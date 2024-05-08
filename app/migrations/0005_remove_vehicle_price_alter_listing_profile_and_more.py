# Generated by Django 5.0.3 on 2024-05-08 01:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0004_profile_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="vehicle",
            name="price",
        ),
        migrations.AlterField(
            model_name="listing",
            name="profile",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="app.profile",
                verbose_name="user",
            ),
        ),
        migrations.AlterField(
            model_name="listing",
            name="vehicle",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="app.vehicle",
                verbose_name="vehicle",
            ),
        ),
    ]
