# Generated by Django 4.0.5 on 2022-12-20 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0047_alter_details_birth_alter_details_exp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
