# Generated by Django 4.0.5 on 2022-11-22 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0031_remove_connection_username_connection_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='connection',
            name='user',
        ),
        migrations.AddField(
            model_name='connection',
            name='username',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
