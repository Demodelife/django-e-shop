from rest_framework import serializers
from app_orders.models import Order, Payment


class OrderSerializer(serializers.ModelSerializer):
    """
    Сериализатор заказа
    """
    orderId = serializers.CharField(source='id', read_only=True)
    products = serializers.SerializerMethodField('get_products')

    class Meta:
        model = Order
        fields = (
            'orderId',
            'createdAt',
            'fullName',
            'email',
            'phone',
            'deliveryType',
            'paymentType',
            'totalCost',
            'status',
            'city',
            'address',
            'products'
        )

    def get_products(self, obj):
        return [
            {
                'id': str(op.product.id),
                'category': str(op.product.category.id),
                'price': float(op.price),
                'count': op.count,
                'date': op.product.date.strftime('%d.%m.%Y %H:%M:%S'),
                'title': op.product.title,
                'description': op.product.fullDescription[:100],
                'href': op.product.href,
                'freeDelivery': op.product.freeDelivery,
                'images': [str(image.image.url) for image in op.product.images.all()],
                'tags': [tag.name for tag in op.product.tags.all()],
                'reviews': op.product.reviews.count(),
                'rating': op.product.rating,
            }
            for op in obj.products.all()
        ]


class PaymentSerializer(serializers.ModelSerializer):
    """
    Сериализатор оплаты
    """

    class Meta:
        model = Payment
        fields = (
            'card',
            'name',
            'month',
            'year',
            'code'
        )


