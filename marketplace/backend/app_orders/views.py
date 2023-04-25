from django.db import transaction
from django.db.models import QuerySet
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.request import Request
from rest_framework.response import Response
from app_cart.cart import Cart
from app_orders.models import Order, OrderProduct, Payment
from app_orders.serializers import OrderSerializer, PaymentSerializer
from app_products.models import Product



class OrderActiveAPIView(GenericAPIView):
    """
    Получение активного заказа пользователя.
    """
    serializer_class = OrderSerializer

    def get(self, request: Request, *args, **kwargs) -> Response:
        if not self.request.user.is_authenticated:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        user = self.request.user.profile

        active_order = Order.objects.filter(user=user, status='accepted').order_by('-id').first()
        serializer = self.serializer_class(active_order)

        return Response(serializer.data, status=status.HTTP_200_OK)


class OrderListCreateAPIView(ListCreateAPIView):
    """
    Представление для получения списка заказов
    и создания нового заказа пользователем.
    """
    serializer_class = OrderSerializer


    def get_queryset(self) -> QuerySet[Order]:

        queryset = (
            Order.objects
            .filter(user=self.request.user.profile)
            .select_related('user')
            .prefetch_related(
                'products__product__category',
                'products__product__images',
                'products__product__tags',
                'products__product__reviews',
            )
            .order_by('-createdAt')
        )[:10]
        return queryset


    def post(self, request: Request, *args, **kwargs) -> Response:
        user = self.request.user.profile
        data = self.request.data
        order, created = Order.objects.get_or_create(user=user, status='accepted')
        order_products = []

        if created:
            for product in data:
                order_products.append(
                    OrderProduct(
                        order=order,
                        product=Product.objects.get(id=product['id']),
                        count=product['count'],
                        price=product['price'],
                    )
                )

            OrderProduct.objects.bulk_create(order_products)
        serializer = self.serializer_class(order)

        return Response(serializer.data, status=status.HTTP_200_OK)


class OrderConfirmRetrieveAPIView(RetrieveModelMixin, GenericAPIView):
    """
    Представление получения детальной информации по заказу пользователя
    и подтверждения заказа пользователем.
    """
    serializer_class = OrderSerializer


    def get_queryset(self):
        queryset = (
            Order.objects
            .filter(user=self.request.user.profile)
            .select_related('user')
            .prefetch_related('products')
        )
        return queryset


    def get(self, request: Request, *args, **kwargs) -> Response:
        return self.retrieve(request, *args, **kwargs)


    def post(self, request: Request, *args, **kwargs) -> Response:
        user = self.request.user.profile
        data = self.request.data

        order = Order.objects.get(user=user, status='accepted')
        order.status = 'waiting for payment'
        order.fullName = data.get('fullName', user.fullName)
        order.email = data.get('email', user.email)
        order.phone = data.get('phone', user.phone)
        order.totalCost = (sum([product['price'] for product in data['products']]))
        order.address = data.get('address', '')
        order.city = data.get('city', '')
        order.deliveryType = data.get('deliveryType', 'ordinary')
        order.paymentType = data.get('paymentType', 'online')
        order.save()

        return Response(status=status.HTTP_201_CREATED)


class PaymentAPIView(GenericAPIView):
    """
    Представление оплаты заказа.
    """
    serializer_class = PaymentSerializer

    @transaction.atomic
    def post(self, request: Request, *args, **kwargs) -> Response:
        cart = Cart(request)
        user = self.request.user.profile
        data = self.request.data
        order = Order.objects.filter(user=user, status='waiting for payment').last()
        serializer = self.serializer_class(data=data)
        order_products = OrderProduct.objects.filter(order=order)

        if serializer.is_valid():
            for product in order_products.all():
                Payment.objects.get_or_create(
                    order=product.order,
                    name=serializer.validated_data['name'],
                    card=serializer.validated_data['card'],
                    code=serializer.validated_data['code'],
                    month=serializer.validated_data['month'],
                    year=serializer.validated_data['year'],
                )

                if product.product.count >= product.count:
                    product.product.count -= product.count
                    if not product.product.count:
                        product.product.available = False
                else:
                    product.product.count = 0
                    product.product.available = False

                product.product.save()

            order.status = 'paid'
            order.save()
            cart.clear()

            return Response({'detail': 'Payment was successful'})
        return Response(status=status.HTTP_400_BAD_REQUEST)
