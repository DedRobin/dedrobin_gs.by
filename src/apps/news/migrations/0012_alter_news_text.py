# Generated by Django 4.2.2 on 2023-06-29 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0011_alter_news_text"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="text",
            field=models.TextField(blank=True, default=""),
        ),
    ]