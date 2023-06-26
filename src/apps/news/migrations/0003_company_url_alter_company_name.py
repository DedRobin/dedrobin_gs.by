# Generated by Django 4.2.2 on 2023-06-26 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0002_news_external_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="company",
            name="url",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="company",
            name="name",
            field=models.CharField(db_index=True, unique=True),
        ),
    ]
