# Generated by Django 4.2.3 on 2023-08-25 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("address", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="address",
            options={"verbose_name": "Address", "verbose_name_plural": "Addresses"},
        ),
    ]