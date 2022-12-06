# Generated by Django 4.0.5 on 2022-12-03 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0041_alter_search_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('babysitter', models.CharField(max_length=100)),
                ('parent', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('search', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.search')),
            ],
        ),
    ]
