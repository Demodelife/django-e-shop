# Generated by Django 4.1.7 on 2023-04-10 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_products', '0010_alter_category_href_alter_product_href_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaleItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='product name')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='price')),
                ('salePrice', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='sale price')),
                ('dateFrom', models.DateField(verbose_name='date from')),
                ('dateTo', models.DateField(verbose_name='date to')),
                ('href', models.CharField(default='', max_length=200, unique=True, verbose_name='href')),
            ],
            options={
                'verbose_name': 'sale item',
                'verbose_name_plural': 'sale items',
            },
        ),
    ]
