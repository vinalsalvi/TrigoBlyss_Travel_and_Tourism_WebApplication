# Generated by Django 5.0.3 on 2024-04-05 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_rename_name_profile_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(default='completed', max_length=30),
        ),
    ]
