# Generated by Django 4.2.11 on 2024-04-22 17:27

import core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_customuser_type"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="username",
        ),
        migrations.AlterField(
            model_name="customuser",
            name="national_number",
            field=models.CharField(
                max_length=255,
                unique=True,
                validators=[
                    core.validators.DigitValidator(11),
                    core.validators.LengthValidator(11),
                ],
            ),
        ),
    ]
