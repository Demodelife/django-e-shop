from rest_framework import serializers

from app_products.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор категории товара"""
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор товара"""
    class Meta:
        model = Product
        fields = '__all__'