# Generated by Django 4.2.2 on 2023-07-07 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("club", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="club",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="src/apps/club/static/images/club"
            ),
        ),
    ]
