# Generated by Django 4.2.3 on 2023-07-18 12:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rent", "0011_roomrent_hours_roomrent_people"),
    ]

    operations = [
        migrations.AlterField(
            model_name="roomrent",
            name="hours",
            field=models.IntegerField(
                blank=True,
                null=True,
                validators=[django.core.validators.MinValueValidator(limit_value=1)],
            ),
        ),
        migrations.AlterField(
            model_name="roomrent",
            name="people",
            field=models.IntegerField(
                blank=True,
                null=True,
                validators=[django.core.validators.MinValueValidator(limit_value=1)],
            ),
        ),
    ]
