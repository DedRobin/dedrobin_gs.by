# Generated by Django 4.2.3 on 2023-08-14 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profile", "0003_profile_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="photo",
            field=models.ImageField(
                blank=True, null=True, upload_to="apps/profile/media/"
            ),
        ),
    ]