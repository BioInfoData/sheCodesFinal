# Generated by Django 4.0.5 on 2022-11-21 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('connected_user', models.CharField(max_length=100)),
            ],
        ),
    ]
