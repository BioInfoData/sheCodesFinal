# Generated by Django 4.0.5 on 2022-11-17 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_profile_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='id_user',
        ),
    ]
