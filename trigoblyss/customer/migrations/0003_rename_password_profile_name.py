# Generated by Django 5.0.3 on 2024-04-05 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='password',
            new_name='name',
        ),
    ]
