# Generated by Django 5.0.3 on 2024-04-27 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0009_abc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='abc',
            name='plan',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='plan',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='user',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='booking',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='user',
        ),
        migrations.DeleteModel(
            name='Inquiry',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='login',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='abc',
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
        migrations.DeleteModel(
            name='Feedback',
        ),
        migrations.DeleteModel(
            name='Login',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
