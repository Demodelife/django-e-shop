# Generated by Django 4.1.7 on 2023-04-20 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_orders', '0007_alter_payment_card_alter_payment_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='card',
            field=models.CharField(max_length=20, verbose_name='card number'),
        ),
    ]
