# Generated by Django 4.2.2 on 2023-06-26 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0004_alter_company_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="created_at",
            field=models.DateField(db_index=True),
        ),
    ]
