# Generated by Django 4.2.3 on 2023-07-13 06:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("rent", "0006_alter_clubrent_club_alter_clubrent_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="clubrent",
            name="club",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="rented_clubs",
                to="rent.club",
            ),
        ),
        migrations.AlterField(
            model_name="clubrent",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="rented_clubs",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
