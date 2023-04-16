from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from app_products.views import (
    CategoryListAPIView,
    ProductListAPIView,
    ProductDetailAPIView,
    SaleItemListAPIView,
    ProductTagListAPIView,
    # BannerListAPIView,
    ProductsPopularAPIView,
    ProductsLimitedAPIView, BannerListAPIView, ProductReviewCreateAPIView
)



app_name = 'app_products'


urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='categories'),
    path('catalog/', ProductListAPIView.as_view(), name='catalog'),
    path('catalog/<int:pk>/',ProductDetailAPIView.as_view(), name='product-detail'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('products/<int:pk>/review/', ProductReviewCreateAPIView.as_view(), name='product-review'),
    path('products/popular/',ProductsPopularAPIView.as_view(), name='products-popular'),
    path('products/limited/',ProductsLimitedAPIView.as_view(), name='products-limited'),
    path('sales/', SaleItemListAPIView.as_view(), name='sales'),
    path('tags/', ProductTagListAPIView.as_view(), name='tags'),
    path('banners/', BannerListAPIView.as_view(), name='banners'),
]
