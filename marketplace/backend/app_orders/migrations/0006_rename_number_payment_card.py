# Generated by Django 4.1.7 on 2023-04-20 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_orders', '0005_payment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='number',
            new_name='card',
        ),
    ]
