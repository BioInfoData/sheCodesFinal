# Generated by Django 4.0.5 on 2022-11-22 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0028_alter_connection_connected_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connection',
            name='connected_user',
            field=models.ManyToManyField(to='accounts.profile'),
        ),
    ]
