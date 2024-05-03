# Generated by Django 5.0.3 on 2024-05-02 18:52

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coursework', '0002_user_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Customer',
        ),
        migrations.RenameField(
            model_name='admin',
            old_name='User',
            new_name='Customer',
        ),
        migrations.RenameField(
            model_name='reservation',
            old_name='User',
            new_name='Customer',
        ),
    ]