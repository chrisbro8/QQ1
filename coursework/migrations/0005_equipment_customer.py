# Generated by Django 5.0.3 on 2024-05-02 20:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursework', '0004_customer_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='coursework.customer'),
        ),
    ]