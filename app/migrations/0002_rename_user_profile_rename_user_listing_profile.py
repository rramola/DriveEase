# Generated by Django 5.0.3 on 2024-05-05 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Profile',
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='user',
            new_name='profile',
        ),
    ]
