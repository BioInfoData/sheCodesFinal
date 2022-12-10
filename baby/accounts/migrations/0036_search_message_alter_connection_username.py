# Generated by Django 4.0.5 on 2022-12-01 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0035_details_username_profile_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='message',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='connection',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]