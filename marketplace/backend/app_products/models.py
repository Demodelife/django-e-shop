from django.db import models
from django.utils.translation import gettext_lazy as _


def category_image_directory_path(instance: 'Category', filename: str) -> str:
    return 'categories/category_{pk}/images/{filename}'.format(
        pk=instance.pk,
        filename=filename,
    )


def subcategory_image_directory_path(instance: 'Subcategory', filename: str) -> str:
    return 'subcategories/subcategory_{pk}/images/{filename}'.format(
        pk=instance.pk,
        filename=filename,
    )


def product_images_directory_path(instance: 'ProductImage', filename: str) -> str:
    return 'products/product_{pk}/images/{filename}'.format(
        pk=instance.product.pk,
        filename=filename,
    )


class Category(models.Model):
    """Модель категории товара"""
    title = models.CharField(max_length=200, verbose_name=_('category name'))
    description = models.TextField(blank=True, verbose_name=_('description'))
    image = models.ImageField(null=True, blank=True, verbose_name=_('image'), upload_to=category_image_directory_path)
    href = models.CharField(max_length=200, unique=True, default='', verbose_name=_('href'))

    class Meta:
        verbose_name_plural = _('categories')
        verbose_name = _('category')


class Subcategory(models.Model):
    """Модель подкатегории товара"""
    title = models.CharField(max_length=200, verbose_name=_('subcategory name'))
    description = models.TextField(blank=True, verbose_name=_('description'))
    image = models.ImageField(null=True, blank=True, upload_to=subcategory_image_directory_path, verbose_name=_('image'))
    href = models.CharField(max_length=200, unique=True, default='', verbose_name=_('href'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories', verbose_name=_('category'))

    class Meta:
        verbose_name_plural = _('subcategories')
        verbose_name = _('subcategory')


class Product(models.Model):
    """Модель товара"""
    title = models.CharField(max_length=200, verbose_name=_('product name'))
    description = models.TextField(blank=True, verbose_name=_('description'))
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name=_('price'))
    count = models.PositiveSmallIntegerField(default=1, verbose_name=_('quantity'))
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products', verbose_name=_('category'))
    date = models.DateTimeField(auto_now_add=True, verbose_name=_('date'))
    href = models.CharField(max_length=200, unique=True, default='', verbose_name=_('href'))
    freeDelivery = models.BooleanField(default=False, verbose_name=_('free delivery'))
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0, verbose_name=_('rating'))
    reviews = models.PositiveSmallIntegerField(default=0, verbose_name=_('reviews'))
    tags = models.ManyToManyField('ProductTag', related_name='products', verbose_name=_('tags'))

    class Meta:
        verbose_name_plural = _('products')
        verbose_name = _('product')


class ProductImage(models.Model):
    """Модель картинки товара"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', verbose_name=_('product'))
    image = models.ImageField(null=True, blank=True, upload_to=product_images_directory_path, verbose_name=_('image'))

    class Meta:
        verbose_name_plural = _('product images')
        verbose_name = _('product image')


class ProductTag(models.Model):
    """Модель тэга товара"""
    name = models.CharField(max_length=100, verbose_name=_('tag name'))

    class Meta:
        verbose_name_plural = _('product tags')
        verbose_name = _('product tag')


class SaleItem(models.Model):
    """Модель скидочного товара"""
    title = models.CharField(max_length=200, verbose_name=_('product name'))
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name=_('price'))
    salePrice = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name=_('sale price'))
    dateFrom = models.DateField(verbose_name=_('date from'))
    dateTo = models.DateField(verbose_name=_('date to'))
    href = models.CharField(max_length=200, unique=True, default='', verbose_name=_('href'))

    class Meta:
        verbose_name_plural = _('sale items')
        verbose_name = _('sale item')
