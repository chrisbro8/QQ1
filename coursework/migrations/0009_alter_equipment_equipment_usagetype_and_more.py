# Generated by Django 5.0.3 on 2024-04-15 19:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursework', '0008_remove_adminandequipment_equipmentid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='Equipment_UsageType',
            field=models.IntegerField(choices=[(0, 'Can be Used and borrowed to home'), (1, 'Only used at University')], null=True),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='Equipment_category',
            field=models.CharField(choices=[('PC/Laptop', 'PC/Laptop'), ('VR-Headset', 'VR Headset'), ('Camera/Sensors', 'Camera/Sensors'), ('PC-Peripherals', 'PC Peripherals'), ('Furniture', 'Furniture'), ('Other', 'Other'), ('VR-Controller', 'VR Controller'), ('Phone/Tablets', 'Phone/Tablets'), ('Power/Cable', 'Power/Cable'), ('Non_PortablePC', 'NonPortablePC')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='Equipment_restrictionStatus',
            field=models.IntegerField(choices=[(0, 'Anyone can use this'), (1, 'Can Only be Used by Staff and Admin')], null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='Equipment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='coursework.equipment'),
        ),
    ]