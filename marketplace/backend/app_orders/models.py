from re import fullmatch

from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError
from app_products.models import Product
from app_profiles.models import UserProfile




def validate_card_year(value):
    if not fullmatch(r'^0[1-9]|[1-9][0-9]$', value):
        raise ValidationError('Year must be between 01 and 99')


def validate_card_month(value):
    if not fullmatch(r'^0[1-9]|1[0-2]$', value):
        raise ValidationError('Month must be between 01 and 12')


class Order(models.Model):
    """Модель заказа"""
    user = models.ForeignKey(UserProfile, default=1, on_delete=models.CASCADE, related_name='orders', verbose_name=_('user'))
    createdAt = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))
    fullName = models.CharField(max_length=200, verbose_name=_('full name'))
    email = models.EmailField(blank=False, verbose_name=_('email'))
    phone = models.CharField(max_length=20, verbose_name=_('phone'))
    deliveryType = models.CharField(max_length=20, verbose_name=_('delivery type'))
    paymentType = models.CharField(max_length=20, verbose_name=_('payment type'))
    totalCost = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name=_('total cost'))
    status = models.CharField(max_length=20, verbose_name=_('status'))
    city = models.CharField(max_length=20, verbose_name=_('city'))
    address = models.CharField(max_length=100, verbose_name=_('address'))


    class Meta:
        verbose_name_plural = _('orders')
        verbose_name = _('order')

    def __str__(self):
        return f'Order № {self.pk}'


class OrderProduct(models.Model):
    """Модель товара в заказе"""
    order = models.ForeignKey(Order, related_name='products', on_delete=models.CASCADE, verbose_name=_('order'))
    product = models.ForeignKey(Product, related_name='order_products', on_delete=models.CASCADE, verbose_name=_('product'))
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name=_('price'))
    count = models.PositiveSmallIntegerField(default=1, verbose_name=_('quantity'))

    class Meta:
        verbose_name_plural = _('order products')
        verbose_name = _('order product')

    def __str__(self):
        return f'Order Product "{self.product.title}"'


class Payment(models.Model):
    """Модель оплаты"""
    order = models.OneToOneField(Order, related_name='payment', on_delete=models.CASCADE, verbose_name=_('order'))
    name = models.CharField(max_length=100, verbose_name=_('name'))
    card = models.CharField(max_length=20, verbose_name=_('card number'))
    code = models.CharField(max_length=3, verbose_name=_('code'))
    month = models.CharField(max_length=2, validators=[validate_card_month], verbose_name=_('month'))
    year = models.CharField(max_length=2, validators=[validate_card_year], verbose_name=_('year'))

    class Meta:
        verbose_name_plural = _('payments')
        verbose_name = _('payment')

    def __str__(self):
        return f'Order Payment № {self.pk}'