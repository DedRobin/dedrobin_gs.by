# Generated by Django 4.2.3 on 2023-08-09 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0009_alter_product_product_type_purchase"),
    ]

    operations = [
        migrations.AddField(
            model_name="purchase",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
