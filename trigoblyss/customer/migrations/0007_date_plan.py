# Generated by Django 5.0.3 on 2024-04-27 11:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_date'),
        ('myadmin', '0002_alter_plan_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='date',
            name='plan',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='myadmin.plan'),
        ),
    ]
