# Generated by Django 5.0.3 on 2024-05-02 20:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursework', '0005_equipment_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='Customer',
        ),
        migrations.RemoveField(
            model_name='admin',
            name='Reservation',
        ),
        migrations.AlterField(
            model_name='admin',
            name='Report',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='coursework.report'),
        ),
    ]
