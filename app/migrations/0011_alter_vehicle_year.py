# Generated by Django 5.0.3 on 2024-05-18 15:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0010_rename_account_type_profile_groups"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vehicle",
            name="year",
            field=models.CharField(max_length=4),
        ),
    ]
