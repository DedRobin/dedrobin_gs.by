# Generated by Django 4.2.2 on 2023-07-11 08:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("rent", "0004_rename_cluborder_clubrent_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="clubrent",
            name="club",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="rented_clubs",
                to="rent.club",
            ),
        ),
        migrations.AlterField(
            model_name="clubrent",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="rented_clubs",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="consolerent",
            name="console",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="rented_consoles",
                to="rent.console",
            ),
        ),
        migrations.AlterField(
            model_name="consolerent",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="rented_consoles",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="roomrent",
            name="room",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="rented_rooms",
                to="rent.room",
            ),
        ),
        migrations.AlterField(
            model_name="roomrent",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="rented_rooms",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
