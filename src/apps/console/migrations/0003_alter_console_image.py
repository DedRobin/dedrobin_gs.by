# Generated by Django 4.2.2 on 2023-07-07 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("console", "0002_console_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="console",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="src/apps/console/static/images/console",
            ),
        ),
    ]