# Generated by Django 4.2.3 on 2023-07-13 06:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("rent", "0007_alter_clubrent_club_alter_clubrent_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="roomrent",
            name="room",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="rented_rooms",
                to="rent.room",
            ),
        ),
        migrations.AlterField(
            model_name="roomrent",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="rented_rooms",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
