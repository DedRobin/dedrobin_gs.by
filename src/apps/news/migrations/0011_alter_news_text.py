# Generated by Django 4.2.2 on 2023-06-29 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0010_alter_news_text"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="text",
            field=models.TextField(default=""),
        ),
    ]