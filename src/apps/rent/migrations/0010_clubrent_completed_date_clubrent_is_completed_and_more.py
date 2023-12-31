# Generated by Django 4.2.3 on 2023-07-13 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rent", "0009_alter_clubaddress_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="clubrent",
            name="completed_date",
            field=models.DateTimeField(blank=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name="clubrent",
            name="is_completed",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name="consolerent",
            name="completed_date",
            field=models.DateTimeField(blank=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name="consolerent",
            name="is_completed",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name="roomrent",
            name="completed_date",
            field=models.DateTimeField(blank=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name="roomrent",
            name="is_completed",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
