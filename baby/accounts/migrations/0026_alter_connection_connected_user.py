# Generated by Django 4.0.5 on 2022-11-21 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0025_rename_conection_connection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connection',
            name='connected_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.profile'),
        ),
    ]
