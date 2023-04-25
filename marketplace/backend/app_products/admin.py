from django.contrib import admin

from app_products.models import (
    Category,
    Product,
    ProductImage,
    ProductTag,
    SaleItem,
    SaleItemImage,
    Specification,
    Review,
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'description'
    list_display_links = 'id', 'title'

class ProductInline(admin.StackedInline):
    model = ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductInline,
    ]
    list_display = 'id', 'title', 'price', 'description_short', 'category'
    list_display_links = 'id', 'title'

    def description_short(self, obj: Product) -> str:
        if len(obj.fullDescription) < 50:
            return obj.fullDescription
        return obj.fullDescription[:50] + "..."

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = 'id', 'image'


@admin.register(ProductTag)
class ProductTagAdmin(admin.ModelAdmin):
    list_display = 'id', 'name'
    list_display_links = 'id', 'name'


@admin.register(SaleItem)
class SaleItemAdmin(admin.ModelAdmin):
    list_display = 'id', 'salePrice', 'product'
    list_display_links = 'id', 'product'


@admin.register(SaleItemImage)
class SaleItemImageAdmin(admin.ModelAdmin):
    list_display = 'id', 'image'


@admin.register(Specification)
class SpecificationAdmin(admin.ModelAdmin):
    list_display = 'id', 'product', 'name', 'value'
    list_display_links = 'id', 'product'


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = 'id', 'product', 'rate', 'author'
    list_display_links = 'id', 'product'