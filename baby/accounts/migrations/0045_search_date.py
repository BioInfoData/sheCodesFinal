# Generated by Django 4.0.5 on 2022-12-06 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0044_alter_searchmessage_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
