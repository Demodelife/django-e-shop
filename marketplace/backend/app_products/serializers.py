from time import strftime

from rest_framework import serializers

from app_products.models import Category, Product, Subcategory, ProductTag, ProductImage, SaleItem, SaleItemImage, \
    Review


class SubcategorySerializer(serializers.ModelSerializer):
    """
    Сериализатор подкатегории товара
    """

    class Meta:
        model = Subcategory
        fields = 'id', 'title', 'image', 'href'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['id'] = str(data['id'])
        data['image'] = {}
        return data


class CategorySerializer(serializers.ModelSerializer):
    """
    Сериализатор категории товара
    """
    subcategories = SubcategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = 'id', 'title', 'image', 'href', 'subcategories'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['id'] = str(data['id'])
        data['image'] = {}
        return data


class ProductTagSerializer(serializers.ModelSerializer):
    """
    Сериализатор тэга товара
    """

    class Meta:
        model = ProductTag
        fields = 'id', 'name'


class ProductImageSerializer(serializers.ModelSerializer):
    """
    Сериализатор картинки товара
    """

    class Meta:
        model = ProductImage
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['id'] = str(data['id'])
        return data



class ProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор товара
    """
    tags = ProductTagSerializer(many=True, read_only=True)


    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        # data['price'] = float(data['price'])
        data['id'] = str(data['id'])
        data['category'] = str(data['category'])
        # data['tags'] = [str(tag.name) for tag in instance.tags.all()]
        data['images'] = [str(image.image.url) for image in instance.images.all()]
        data['specifications'] = [{'name': spec.name, 'value': spec.value} for spec in instance.specifications.all()]
        data['reviews'] = [
            {
            'author': rev.author,
            'email': rev.email,
            'text': rev.text,
            'rate': rev.rate,
            'date': rev.date.strftime('%d.%m.%Y %H:%M:%S'),
            }
            for rev in instance.reviews.all()
        ]

        return data


class SaleItemImageSerializer(serializers.ModelSerializer):
    """
    Сериализатор картинки товара со скидкой
    """

    class Meta:
        model = SaleItemImage
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['id'] = str(data['id'])
        return data


class SaleItemSerializer(serializers.ModelSerializer):
    """
    Сериализатор товара со скидкой
    """
    images = SaleItemImageSerializer(many=True, read_only=True)

    class Meta:
        model = SaleItem
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['id'] = str(data['id'])
        data['images'] = [str(image.image.url) for image in instance.images.all()]
        return data


class ReviewSerializer(serializers.ModelSerializer):
    """Сериализатор отзыва к товару"""

    class Meta:
        model = Review
        fields = 'author', 'email', 'text', 'rate'
