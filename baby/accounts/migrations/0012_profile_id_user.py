# Generated by Django 4.0.5 on 2022-11-13 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_remove_profile_birth_remove_profile_id_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='id_user',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
