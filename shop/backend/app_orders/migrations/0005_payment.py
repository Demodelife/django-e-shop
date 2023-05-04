# Generated by Django 4.1.7 on 2023-04-20 15:30

import app_orders.models
import creditcards.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_orders', '0004_order_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('number', creditcards.models.CardNumberField(max_length=25, verbose_name='card number')),
                ('code', creditcards.models.SecurityCodeField(max_length=4, verbose_name='code')),
                ('month', models.CharField(max_length=2, validators=[app_orders.models.validate_card_month], verbose_name='month')),
                ('year', models.CharField(max_length=4, validators=[app_orders.models.validate_card_year], verbose_name='year')),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='app_orders.order', verbose_name='order')),
            ],
            options={
                'verbose_name': 'payment',
                'verbose_name_plural': 'payments',
            },
        ),
    ]