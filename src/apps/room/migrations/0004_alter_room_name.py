# Generated by Django 4.2.2 on 2023-07-07 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("room", "0003_alter_room_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="room",
            name="name",
            field=models.CharField(db_index=True, max_length=150, unique=True),
        ),
    ]