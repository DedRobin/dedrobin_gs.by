# Generated by Django 4.2.3 on 2023-08-22 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rent", "0012_alter_roomrent_hours_alter_roomrent_people"),
    ]

    operations = [
        migrations.AlterField(
            model_name="club",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="rent/media/images/club"
            ),
        ),
        migrations.AlterField(
            model_name="console",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="rent/media/images/console"
            ),
        ),
        migrations.AlterField(
            model_name="room",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="rent/media/images/room"
            ),
        ),
    ]