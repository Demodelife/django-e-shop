from django.contrib import admin

from app_products.models import Category, Product, Subcategory, ProductImage, ProductTag, SaleItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'description'


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'description', 'category'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'description', 'category'


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = 'id', 'image'


@admin.register(ProductTag)
class ProductTagAdmin(admin.ModelAdmin):
    list_display = 'id', 'name'


@admin.register(SaleItem)
class SaleItemAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'price', 'salePrice'