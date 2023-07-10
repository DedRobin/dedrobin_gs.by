# Generated by Django 4.2.2 on 2023-07-10 10:37

from django.db import migrations, models
import django.db.models.deletion
import src.apps.rent.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Club",
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
                ("name", models.CharField(db_index=True, max_length=150, unique=True)),
                ("description", models.TextField()),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="src/apps/rent/media/images/club",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ClubAddress",
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
                ("city", models.CharField(max_length=150)),
                ("street", models.CharField(max_length=150)),
                ("building", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Console",
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
                ("name", models.CharField(db_index=True, max_length=150, unique=True)),
                ("price_per_day", models.DecimalField(decimal_places=2, max_digits=5)),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="src/apps/rent/media/images/console",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Room",
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
                ("name", models.CharField(db_index=True, max_length=150, unique=True)),
                ("number", models.IntegerField()),
                ("seats", models.IntegerField()),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="src/apps/rent/media/images/room",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RoomOrder",
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
                    "room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="orders",
                        to="rent.room",
                    ),
                ),
            ],
            bases=(src.apps.rent.models.Order, models.Model),
        ),
        migrations.CreateModel(
            name="ConsoleOrder",
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
                ("days", models.IntegerField(blank=True, null=True)),
                (
                    "console",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="orders",
                        to="rent.console",
                    ),
                ),
            ],
            bases=(src.apps.rent.models.Order, models.Model),
        ),
        migrations.CreateModel(
            name="ClubOrder",
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
                    "club",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="orders",
                        to="rent.club",
                    ),
                ),
            ],
            bases=(src.apps.rent.models.Order, models.Model),
        ),
        migrations.AddField(
            model_name="club",
            name="address",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="rent.clubaddress"
            ),
        ),
    ]
