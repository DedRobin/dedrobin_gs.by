# Generated by Django 4.2.3 on 2023-07-31 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0004_alter_mouse_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="mouse",
            name="release_date",
        ),
    ]
