from rest_framework import serializers

from app_products.models import Category, Product, Subcategory, ProductTag, ProductImage, SaleItem


class SubcategorySerializer(serializers.ModelSerializer):
    """Сериализатор подкатегории товара"""
    class Meta:
        model = Subcategory
        fields = '__all__'

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['id'] = str(repr['id'])
        return repr


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор категории товара"""
    subcategories = SubcategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['id'] = str(repr['id'])
        return repr


class ProductTagSerializer(serializers.ModelSerializer):
    """Сериализатор тэга товара"""
    class Meta:
        model = ProductTag
        fields = '__all__'

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['id'] = str(repr['id'])
        return repr


class ProductImageSerializer(serializers.ModelSerializer):
    """Сериализатор картинки товара"""
    class Meta:
        model = ProductImage
        fields = '__all__'

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['id'] = str(repr['id'])
        return repr


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор товара"""
    images = ProductImageSerializer(many=True, read_only=True)
    tags = ProductTagSerializer(many=True, read_only=True)


    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['id'] = str(repr['id'])
        repr['category'] = str(repr['category'])
        repr['tags'] = [str(tag.name)for tag in instance.tags.all()]
        repr['images'] = [str(image.image)for image in instance.images.all()]
        return repr


class SaleItemSerializer(serializers.ModelSerializer):
    """Сериализатор товара со скидкой"""

    class Meta:
        model = SaleItem
        fields = '__all__'

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['id'] = str(repr['id'])
        return repr
