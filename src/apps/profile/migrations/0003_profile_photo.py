# Generated by Django 4.2.3 on 2023-08-14 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profile", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="photo",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
