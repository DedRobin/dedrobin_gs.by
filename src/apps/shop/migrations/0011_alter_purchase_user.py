# Generated by Django 4.2.3 on 2023-08-17 08:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("shop", "0010_purchase_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="purchase",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="purchases",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
