# Generated by Django 4.2.2 on 2023-06-17 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("profile", "0003_alter_profile_gander"),
    ]

    operations = [
        migrations.RenameField(
            model_name="profile",
            old_name="gander",
            new_name="gender",
        ),
    ]