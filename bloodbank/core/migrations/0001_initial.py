# Generated by Django 4.2.11 on 2024-04-22 16:36

import core.validators
import django.contrib.auth.validators
import django.utils.timezone
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "first_name",
                    models.CharField(max_length=150, verbose_name="first name"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=150, verbose_name="last name"),
                ),
                (
                    "middle_name",
                    models.CharField(
                        max_length=255, validators=[core.validators.StringValidator(50)]
                    ),
                ),
                ("age", models.PositiveSmallIntegerField()),
                (
                    "blood_type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("A+", "A-positive"),
                            ("A-", "A-negative"),
                            ("B+", "B-positive"),
                            ("B-", "B-negative"),
                            ("AB+", "AB-positive"),
                            ("AB-", "AB-negative"),
                            ("O+", "O-positive"),
                            ("O-", "O-negative"),
                        ],
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "mother_name",
                    models.CharField(
                        max_length=255, validators=[core.validators.StringValidator(50)]
                    ),
                ),
                (
                    "national_number",
                    models.CharField(
                        max_length=255,
                        validators=[
                            core.validators.DigitValidator(11),
                            core.validators.LengthValidator(11),
                        ],
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region="SY"
                    ),
                ),
                ("id_image", models.ImageField(null=True, upload_to="")),
                ("address", models.TextField(null=True)),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Male"), ("", "Unknown")],
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
        ),
    ]
