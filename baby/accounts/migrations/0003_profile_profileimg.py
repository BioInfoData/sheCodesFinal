# Generated by Django 4.0.5 on 2022-10-25 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_gender_alter_profile_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profileimg',
            field=models.ImageField(blank=True, default='defaul_profile.jpg', upload_to=''),
        ),
    ]
