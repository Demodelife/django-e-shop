from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from app_cart.cart import Cart
from app_products.models import Product



class CartAPIView(APIView):
    """
    Представление для работы с корзиной.
    """

    def get(self, request):
        """
        Получить содержимое корзины.
        """
        cart = Cart(request)
        data = list(cart.cart.values())
        # data = sorted(cart.cart.values(), key=lambda x: float(x['price']), reverse=True)

        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Добавить товар в корзину.
        """
        cart = Cart(request)
        product = get_object_or_404(Product, id=request.data['id'])
        count_request = request.data['count']
        count = 1

        if count_request > 1:
            count = count_request

        cart.add(product=product, count=count)
        data = list(cart.cart.values())
        # data = sorted(cart.cart.values(), key=lambda x: float(x['price']), reverse=True)

        return Response(data, status=status.HTTP_200_OK)

    def delete(self, request):
        """
        Удалить товар из корзины.
        """
        cart = Cart(request)
        product = get_object_or_404(Product, id=request.data['id'])
        count_request = request.data['count']
        count = 1

        if count_request > 1:
            count = count_request

        cart.remove(product=product, count=count)
        data = list(cart.cart.values())
        # data = sorted(cart.cart.values(), key=lambda x: float(x['price']), reverse=True)

        return Response(data, status=status.HTTP_200_OK)
