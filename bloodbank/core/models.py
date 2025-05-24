from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager, User
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.functional import cached_property
from django_extensions.db.models import TimeStampedModel
from phonenumber_field.modelfields import PhoneNumberField
from solo.models import SingletonModel

from .validators import DigitValidator, LengthValidator, StringValidator

# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(email=self.normalize_email(email), **kwargs)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **kwargs):
        user = self.create_user(email, password=password, **kwargs)
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


BLOOD_TYPES = [
    ("A+", "A-positive"),
    ("A-", "A-negative"),
    ("B+", "B-positive"),
    ("B-", "B-negative"),
    ("AB+", "AB-positive"),
    ("AB-", "AB-negative"),
    ("O+", "O-positive"),
    ("O-", "O-negative"),
]


class CustomUser(AbstractUser):
    MALE, FEMALE, UNKNOWN = "M", "F", ""
    GENDER_CHOICES = [
        (MALE, "Male"),
        (FEMALE, "Female"),
        (UNKNOWN, "Unknown"),
    ]
    DONOR = "D"
    NURSE = "N"
    USER_TYPES = [
        (
            DONOR,
            "Donor",
        ),
        (
            NURSE,
            "Nurse",
        ),
    ]
    first_name = models.CharField("first name", max_length=150)
    last_name = models.CharField("last name", max_length=150)
    middle_name = models.CharField(max_length=255, validators=[StringValidator(50)])
    age = models.PositiveSmallIntegerField()
    blood_type = models.CharField(
        max_length=255, choices=BLOOD_TYPES, null=True, blank=True
    )
    mother_name = models.CharField(max_length=255, validators=[StringValidator(50)])
    national_number = models.CharField(
        max_length=255,
        validators=[DigitValidator(11), LengthValidator(11)],
        unique=True,
    )
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField(region="SY")
    id_image = models.ImageField(null=True)
    address = models.TextField(null=True)
    gender = models.CharField(null=True, choices=GENDER_CHOICES, max_length=255)
    type = models.CharField(null=True, blank=True, choices=USER_TYPES, max_length=255)
    warn_count = models.PositiveSmallIntegerField(default=0)
    username = None

    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "age",
        "middle_name",
        "mother_name",
        "national_number",
        "phone_number",
        "first_name",
        "last_name",
    ]

    @property
    def is_nurse(self):
        return self.type == self.NURSE

    @property
    def is_donor(self):
        return self.type == self.DONOR

    @cached_property
    def last_donation(self):
        return self.bloodbag_set.order_by("-created").first()

    def can_donate(self, date):
        if not self.is_active:
            return False

        if self.last_donation:
            elapsed = date - self.last_donation.created.date()
            months = elapsed.days // 30
            if months < HospitalSettings.get_solo().months_between_donations:
                return False

        nurse_count = self.__class__.objects.filter(type=self.NURSE).count()
        allowed_reservations = (
            nurse_count
            * HospitalSettings.get_solo().number_of_completed_blood_bags_per_nurse
        )
        number_of_reservations = Reservation.objects.filter(
            status=Reservation.PENDING
        ).count()
        if allowed_reservations <= number_of_reservations:
            return False

        return True

    def give_warning(self):
        self.warn_count += 1
        subject = "Warning"
        message = "You have been warned for missing your reservation, another time will cause a block"
        if self.warn_count > 1:
            message = "You have been blocked for missing your reservation"
            self.is_active = False
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [self.email],
            fail_silently=True,
        )
        self.save()


class Reservation(TimeStampedModel):
    PENDING, DONE, MISSED = "P", "D", "M"
    STATUS_CHOICES = [
        (PENDING, "Pending"),
        (DONE, "Done"),
        (MISSED, "Missed"),
    ]
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default=PENDING)
    donor = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="reservations"
    )
    date = models.DateField()

    def __str__(self):
        return f"{self.status} Reservation for {self.donor}"

    def mark_missed(self):
        self.status = self.MISSED
        self.save()
        self.donor.give_warning()


class HospitalSettings(SingletonModel):
    blood_expiration_duration = models.DurationField(null=True)
    number_of_completed_blood_bags_per_nurse = models.IntegerField(default=15)
    months_between_donations = models.IntegerField(default=3)

    def calculate_expiration_date_from_now(self):
        return timezone.now().date() + self.blood_expiration_duration

    def __str__(self):
        return "Hospital Settings"


class BloodBagQuerySet(models.QuerySet):
    def expired(self):
        now = timezone.now().date()
        return self.filter(expiration_date__lt=now)

    def valid(self):
        now = timezone.now()
        return self.filter(expiration_date__gte=now)

    def annotate_expired(self):
        now = timezone.now()
        return self.annotate(
            expired=models.Case(
                models.When(expiration_date__lt=now, then=True),
                default=False,
                output_field=models.BooleanField(),
            )
        )


class BloodBag(TimeStampedModel):
    blood_type = models.CharField(max_length=255, choices=BLOOD_TYPES)
    donor = models.ForeignKey(
        CustomUser, null=True, blank=True, on_delete=models.SET_NULL
    )
    source = models.CharField(max_length=255, null=True, blank=True)
    expiration_date = models.DateField(help_text="Auto calculated if null", blank=True)

    objects = BloodBagQuerySet.as_manager()

    def calculate_expiration_date(self):
        expiration_date = (
            self.created + HospitalSettings.get_solo().blood_expiration_duration
        )
        return expiration_date

    @property
    def is_expired(self):
        return self.expiration_date < timezone.now().date()

    def __str__(self):
        return f"Blood {self.blood_type}" + (" EXPIRED" if self.is_expired else "")

    def save(self, **kwargs):
        if not self.expiration_date:
            self.expiration_date = (
                self.calculate_expiration_date()
                if self.created
                else HospitalSettings.get_solo().calculate_expiration_date_from_now()
            )
        return super().save(**kwargs)


class TermQuestion(models.Model):
    question = models.TextField()

    def __str__(self):
        return self.question
