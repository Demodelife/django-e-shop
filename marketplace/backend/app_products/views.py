from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpRequest
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from app_products.models import Category, Product, Subcategory, SaleItem
from app_products.serializers import CategorySerializer, ProductSerializer, SaleItemSerializer


class CategoryListAPIView(ListModelMixin, GenericAPIView):
    """Представление списка категорий товара"""
    serializer_class = CategorySerializer
    queryset = Category.objects.order_by('id').all()

    def get(self, request: HttpRequest) -> Response:
        return self.list(request)


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class ProductListAPIView(ListModelMixin, GenericAPIView):
    """Представление списка товаров"""
    serializer_class = ProductSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = Product.objects.order_by('id').all()
        filters = dict()
        name = self.request.query_params.get('name')
        min_price = self.request.query_params.get('minPrice')
        max_price = self.request.query_params.get('maxPrice')
        free_delivery = self.request.query_params.get('freeDelivery')
        available = self.request.query_params.get('available')

        filters.update({
            'title__icontains': name,
            'price__gte': min_price,
            'price__lte': max_price,
            'free_delivery': free_delivery,
            'available': available,
        })
        filters = {k: v for k, v in filters.items() if v is not None}
        queryset = queryset.filter(Q(**filters))

        return queryset

    def get(self, request: HttpRequest):
        return self.list(request)

    def get_paginated_response(self, data):
        return Response({
            'items': data,
            'currentPage': 1,
            'lastPage': 1
        })



class ProductDetailAPIView(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    """
    Представление для получения детальной информации о товаре,
    а также для его редактирования и удаления.
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get(self, request: HttpRequest, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request: HttpRequest, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request: HttpRequest, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class SaleItemListAPIView(ListModelMixin, GenericAPIView):
    """Представление списка скидочных товаров"""
    serializer_class = SaleItemSerializer
    queryset = SaleItem.objects.all()

    def get(self, request: HttpRequest):
        return self.list(request)
