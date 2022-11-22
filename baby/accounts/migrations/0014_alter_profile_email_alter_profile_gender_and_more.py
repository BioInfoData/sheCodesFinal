# Generated by Django 4.0.5 on 2022-11-15 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_profile_slug_alter_profile_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=300),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='type',
            field=models.CharField(blank=True, choices=[('Parent', 'Parent'), ('Babysitter', 'Babysitter')], max_length=300),
        ),
    ]