# Generated by Django 4.0.5 on 2022-11-21 11:56

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0024_conection_delete_conections'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Conection',
            new_name='Connection',
        ),
    ]
