# Generated by Django 4.2.3 on 2023-07-31 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0005_remove_mouse_release_date"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="mouse",
            name="interface",
        ),
        migrations.RemoveField(
            model_name="mouse",
            name="length_or_radius",
        ),
        migrations.RemoveField(
            model_name="mouse",
            name="max_sensor_resolution",
        ),
        migrations.RemoveField(
            model_name="mouse",
            name="sensor_type",
        ),
    ]