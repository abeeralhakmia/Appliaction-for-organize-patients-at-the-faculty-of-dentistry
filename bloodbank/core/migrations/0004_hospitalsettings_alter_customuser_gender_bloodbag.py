# Generated by Django 4.2.11 on 2024-04-22 18:12

import django.db.models.deletion
import django_extensions.db.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_remove_customuser_username_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="HospitalSettings",
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
                ("blood_expiration_duration", models.DurationField(null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AlterField(
            model_name="customuser",
            name="gender",
            field=models.CharField(
                choices=[("M", "Male"), ("F", "Female"), ("", "Unknown")],
                max_length=255,
                null=True,
            ),
        ),
        migrations.CreateModel(
            name="BloodBag",
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
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name="modified"
                    ),
                ),
                (
                    "blood_type",
                    models.CharField(
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
                    ),
                ),
                ("source", models.CharField(blank=True, max_length=255, null=True)),
                ("expiration_date", models.DateField()),
                (
                    "donor",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "get_latest_by": "modified",
                "abstract": False,
            },
        ),
    ]
