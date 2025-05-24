from braces.forms import UserKwargModelFormMixin
from django import forms

from .models import BLOOD_TYPES, CustomUser, Reservation


class DonorForm(forms.ModelForm):
    user_type = CustomUser.DONOR
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirm = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super(DonorForm, self).clean()
        password_confirm = cleaned_data.pop("password_confirm")
        if cleaned_data.get("password") != password_confirm:
            self.add_error("password_confirm", "Passwords doesn't match")

    class Meta:
        model = CustomUser
        fields = (
            "first_name",
            "last_name",
            "middle_name",
            "age",
            "mother_name",
            "national_number",
            "email",
            "phone_number",
            "id_image",
            "address",
            "gender",
            "password",
            "password_confirm",
        )

    def save(self, commit=True):
        password = self.cleaned_data.pop("password")
        user: CustomUser = super(DonorForm, self).save(commit=False)
        user.is_active = False
        user.type = self.user_type
        user.set_password(password)
        if commit:
            user.save()
        return user


class NurseForm(DonorForm):
    user_type = CustomUser.NURSE


class ReserveForm(UserKwargModelFormMixin, forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))

    class Meta:
        model = Reservation
        fields = ("date",)

    def clean(self):
        if not self.user.can_donate(self.cleaned_data["date"]):
            self.add_error("date", "You can't donate at that date")
        return super().clean()

    def save(self, commit=True):
        reservation: Reservation = super().save(commit=False)
        reservation.donor = self.user
        if commit:
            reservation.save()
        return reservation


class ReserveStatusForm(UserKwargModelFormMixin, forms.ModelForm):
    blood_type = forms.ChoiceField(choices=BLOOD_TYPES)
    status = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = Reservation
        fields = (
            "status",
            "blood_type",
        )

    def save(self, commit=True):
        blood_type = self.cleaned_data.pop("blood_type", None)
        instance = super().save(commit=False)
        donor = instance.donor

        if blood_type:
            donor.blood_type = blood_type

        if instance.status == Reservation.MISSED:
            donor.warn_count += 1

        if commit:
            donor.save()
            instance.save()

        return instance
