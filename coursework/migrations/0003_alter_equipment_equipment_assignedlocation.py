# Generated by Django 5.0.3 on 2024-04-15 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursework', '0002_admin_adminandequipment_equipment_report_reservation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='Equipment_assignedlocation',
            field=models.CharField(choices=[('Other', 'Other'), ('XR Lab', 'XR Lab'), ('XR Lab Blue Cabinet', 'XR Lab Blue Cabinet'), ('XR Lab Blue Cabinet Large', 'XR Lab Blue Cabinet Large'), ('XR medium wooden cabinet', 'XR medium wooden cabinet')], max_length=30, null=True),
        ),
    ]