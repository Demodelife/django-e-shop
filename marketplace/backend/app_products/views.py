from django.http import HttpRequest
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response

from app_products.models import Category, Product
from app_products.serializers import CategorySerializer, ProductSerializer


class CategoryListAPIView(ListModelMixin, GenericAPIView):
    """Представление списка категорий товара"""
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get(self, request: HttpRequest) -> Response:
        return self.list(request)


class ProductListAPIView(ListModelMixin, GenericAPIView):
    """Представление списка товаров"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get(self, request: HttpRequest) -> Response:
        return self.list(request)
