from typing import Any
from django.db.models import Q, Avg, Count, QuerySet
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.request import Request
from rest_framework.response import Response
from app_products.models import (
    Category,
    Product,
    SaleItem,
    ProductTag,
)
from app_products.serializers import (
    CategorySerializer,
    ProductSerializer,
    SaleItemSerializer,
    ProductTagSerializer,
    ReviewSerializer,
)


class CustomPagination(PageNumberPagination):
    """
    Класс пагинации
    """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class CategoryListAPIView(ListAPIView):
    """
    Представление списка категорий товаров.
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.order_by('id')

    def get(self, request: Request, *args, **kwargs) -> Response:
        return self.list(request)


class ProductListAPIView(ListAPIView):
    """
    Представление списка товаров
    """
    serializer_class = ProductSerializer
    pagination_class = CustomPagination


    def get_queryset(self) -> QuerySet[Product]:
        queryset = (
           Product.objects
           .filter(available=True)
           .select_related(
               'category',
               'sale_items',
           )
           .prefetch_related(
               'reviews',
               'tags',
               'images',
               'specifications',
           )
        )

        filters = dict()
        name = self.request.query_params.get('filter[name]')
        min_price = self.request.query_params.get('filter[minPrice]')
        max_price = self.request.query_params.get('filter[maxPrice]')
        free_delivery = self.request.query_params.get('filter[freeDelivery]')
        available = self.request.query_params.get('filter[available]')
        tags = self.request.query_params.get('tags[]')

        if free_delivery == 'true':
            free_delivery = True
        else:
            free_delivery = False

        if available == 'true':
            available = 1
        else:
            available = 0

        filters.update({
            'title__icontains': name,
            'price__gte': min_price,
            'price__lte': max_price,
            'freeDelivery': free_delivery,
            'count__gte': available,
            'tags': tags
        })

        filters = {k: v for k, v in filters.items() if v is not None}
        queryset = queryset.filter(Q(**filters))

        sort = self.request.query_params.get('sort')
        sort_type = self.request.query_params.get('sortType')

        if sort == 'rating':
            queryset = queryset.annotate(avg_rating=Avg('reviews__rate')).order_by(
                'avg_rating' if sort_type == 'dec' else '-avg_rating'
            )
        elif sort == 'price':
            queryset = queryset.order_by('price' if sort_type == 'dec' else '-price')
        elif sort == 'reviews':
            queryset = queryset.annotate(num_reviews=Count('reviews')).order_by(
                'num_reviews' if sort_type == 'dec' else '-num_reviews'
            )
        else:
            queryset = queryset.order_by('date' if sort_type == 'dec' else '-date')

        return queryset

    def get(self, request: Request, *args, **kwargs) -> Response:
        return self.list(request)

    def get_paginated_response(self, data) -> Response:
        return Response({
            'items': data,
            'currentPage': 1,
            'lastPage': 1
        })



class ProductDetailAPIView(RetrieveAPIView):
    """
    Представление для получения детальной информации о товаре.
    """
    serializer_class = ProductSerializer
    queryset = (
        Product.objects
        .filter(available=True)
        .select_related(
            'category',
            'sale_items',
        )
        .prefetch_related(
            'reviews',
            'tags',
            'images',
            'specifications',
        )
    )

    def get(self, request: Request, *args, **kwargs) -> Response:
        return self.retrieve(request, *args, **kwargs)


class SaleItemListAPIView(ListAPIView):
    """
    Представление списка скидочных товаров.
    """
    serializer_class = SaleItemSerializer
    queryset = (
        SaleItem.objects
        .select_related('product')
        .prefetch_related('images')
    )

    def get(self, request: Request, *args, **kwargs) -> Response:
        return self.list(request)


class ProductTagListAPIView(ListAPIView):
    """
    Представление списка тэгов товаров.
    """
    serializer_class = ProductTagSerializer
    queryset = ProductTag.objects.order_by('id')

    def get(self, request: Request, *args, **kwargs) -> Response:
        return self.list(request)


class BannerListAPIView(ListAPIView):
    """
    Представление баннера.
    """
    serializer_class = ProductSerializer
    queryset = (
        Product.objects
        .filter(available=True)
        .select_related(
            'category',
            'sale_items',
        )
        .prefetch_related(
            'reviews',
            'tags',
            'images',
            'specifications',
        )
        .order_by('price')
    )[:3]

    def get(self, request: Request, *args, **kwargs) -> Response:
        return self.list(request)


class ProductsPopularAPIView(ListAPIView):
    """
    Представление для получения популярных товаров.
    """
    serializer_class = ProductSerializer
    queryset = (
        Product.objects
        .filter(available=True)
        .select_related(
            'category',
            'sale_items',
        )
        .prefetch_related(
            'reviews',
            'tags',
            'images',
            'specifications',
        )
        .order_by('-rating')
    )[:10]

    def get(self, request: Request, *args, **kwargs) -> Response:
        return self.list(request)


class ProductsLimitedAPIView(ListAPIView):
    """
    Представление для получения ограниченных товаров.
    """
    serializer_class = ProductSerializer
    queryset = (
        Product.objects
        .filter(isLimited=True)
        .select_related(
            'category',
            'sale_items',
        )
        .prefetch_related(
            'reviews',
            'tags',
            'images',
            'specifications',
        )
    )[:3]


    def get(self, request: Request, *args, **kwargs) -> Response:
        return self.list(request)


class ProductReviewCreateAPIView(CreateAPIView):
    """
    Представление для создания отзыва к товару.
    """
    serializer_class = ReviewSerializer

    def perform_create(self, serializer) -> None:
        serializer.save(product=self.get_product())

    def get_product(self) -> Any:
        return get_object_or_404(Product, pk=self.kwargs['pk'])

    def post(self, request: Request, *args, **kwargs) -> Response:
        product = self.get_product()

        if product.reviews.count() != 0:
            product.rating = product.reviews.aggregate(Avg('rate'))['rate__avg']
        else:
            product.rating = self.request.data['rate']

        product.save()

        return self.create(request)