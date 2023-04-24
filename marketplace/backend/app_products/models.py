from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _



def category_image_directory_path(instance: 'Category', filename: str) -> str:
    return 'categories/category_{pk}/images/{filename}'.format(
        pk=instance.pk,
        filename=filename,
    )


def product_images_directory_path(instance: 'ProductImage', filename: str) -> str:
    return 'products/product_{pk}/images/{filename}'.format(
        pk=instance.product.pk,
        filename=filename,
    )

def validate_rate(value):
    if value not in range(1, 6):
        raise ValidationError('Rate can be in range from 1 to 5')


def sale_item_images_directory_path(instance: 'SaleItemImage', filename: str) -> str:
    return 'sale_items/sale_item_{pk}/images/{filename}'.format(
        pk=instance.saleItem.pk,
        filename=filename,
    )


class Category(models.Model):
    """Модель категории товара"""
    title = models.CharField(max_length=200, verbose_name=_('category name'))
    description = models.TextField(blank=True, verbose_name=_('description'))
    image = models.ImageField(null=True, blank=True, verbose_name=_('image'), upload_to=category_image_directory_path)
    subcategories = models.ManyToManyField('self', symmetrical=False, blank=True, verbose_name=_('subcategories'))
    available = models.BooleanField(default=True, verbose_name=_('available'))

    class Meta:
        verbose_name_plural = _('categories')
        verbose_name = _('category')

    @property
    def href(self):
        return f'/catalog/{self.pk}'

    def __str__(self):
        return f'Category "{self.title}"'


class Product(models.Model):
    """Модель товара"""
    title = models.CharField(max_length=200, verbose_name=_('product name'))
    description = models.TextField(blank=True, verbose_name=_('description'))
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name=_('price'))
    count = models.PositiveSmallIntegerField(default=1, verbose_name=_('quantity'))
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products', verbose_name=_('category'))
    date = models.DateTimeField(auto_now_add=True, verbose_name=_('date'))
    freeDelivery = models.BooleanField(default=False, verbose_name=_('free delivery'))
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0, verbose_name=_('rating'))
    tags = models.ManyToManyField('ProductTag', related_name='products', verbose_name=_('tags'))
    available = models.BooleanField(default=True, verbose_name=_('available'))
    isLimited = models.BooleanField(default=False, verbose_name=_('is limited'))

    class Meta:
        verbose_name_plural = _('products')
        verbose_name = _('product')

    @property
    def href(self):
        return f'/product/{self.pk}'

    def __str__(self):
        return f'Product "{self.title}"'


class ProductImage(models.Model):
    """Модель картинки товара"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', verbose_name=_('product'))
    image = models.ImageField(null=True, blank=True, upload_to=product_images_directory_path, verbose_name=_('image'))

    class Meta:
        verbose_name_plural = _('product images')
        verbose_name = _('product image')

    def __str__(self):
        return f'Image for the "{self.product.title}"'


class ProductTag(models.Model):
    """Модель тэга товара"""
    name = models.CharField(max_length=100, verbose_name=_('tag name'))
    available = models.BooleanField(default=True, verbose_name=_('available'))

    class Meta:
        verbose_name_plural = _('product tags')
        verbose_name = _('product tag')

    def __str__(self):
        return f'Tag "{self.name}"'


class SaleItem(models.Model):
    """Модель скидочного товара"""
    product = models.OneToOneField(Product, related_name='sale_items', on_delete=models.CASCADE, verbose_name=_('product'))
    salePrice = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name=_('sale price'))
    dateFrom = models.DateField(verbose_name=_('date from'))
    dateTo = models.DateField(verbose_name=_('date to'))
    available = models.BooleanField(default=True, verbose_name=_('available'))

    class Meta:
        verbose_name_plural = _('sale items')
        verbose_name = _('sale item')

    @property
    def href(self):
        return f'/product/{self.product.pk}'

    def __str__(self):
        return f'Sale Item "{self.product.title}"'


class SaleItemImage(models.Model):
    """Модель картинки скидочного товара"""
    saleItem = models.ForeignKey(SaleItem, on_delete=models.CASCADE, related_name='images', verbose_name=_('product'))
    image = models.ImageField(null=True, blank=True, upload_to=sale_item_images_directory_path, verbose_name=_('image'))

    class Meta:
        verbose_name_plural = _('sale item images')
        verbose_name = _('sale item image')

    def __str__(self):
        return f'Image for sale item "{self.saleItem.product.title}"'


class Specification(models.Model):
    """Модель характеристики товара"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='specifications', verbose_name=_('product'))
    name = models.CharField(max_length=200, verbose_name=_('name'))
    value = models.CharField(max_length=200, null=True, blank=True, verbose_name=_('value'))
    available = models.BooleanField(default=True, verbose_name=_('available'))

    class Meta:
        verbose_name_plural = _('specifications')
        verbose_name = _('specification')

    def __str__(self):
        return f'Specification "{self.name}"'


class Review(models.Model):
    """Модель отзыва к товару"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews', verbose_name=_('product'))
    author = models.CharField(blank=False, max_length=200, verbose_name=_('author'))
    email = models.EmailField(blank=False, verbose_name=_('email'))
    text = models.TextField(blank=True, verbose_name=_('text'))
    rate = models.DecimalField(max_digits=1, decimal_places=0, validators=[validate_rate], verbose_name=_('rate'))
    date = models.DateTimeField(auto_now_add=True, verbose_name=_('date'))
    available = models.BooleanField(default=True, verbose_name=_('available'))

    class Meta:
        verbose_name_plural = _('reviews')
        verbose_name = _('review')

    def __str__(self):
        return f'"{self.product.title}" review'