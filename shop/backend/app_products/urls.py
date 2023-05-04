from django.urls import path
from app_products.views import (
    CategoryListAPIView,
    ProductDetailAPIView,
    SaleItemListAPIView,
    ProductTagListAPIView,
    ProductsPopularAPIView,
    ProductsLimitedAPIView,
    BannerListAPIView,
    ProductReviewCreateAPIView,
    CatalogCategoryListAPIView, CatalogBaseListAPIView
)



app_name = 'app_products'


urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='categories'),
    path('catalog/', CatalogBaseListAPIView.as_view(), name='catalog'),
    path('catalog/<int:pk>/', CatalogCategoryListAPIView.as_view(), name='catalog-category'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('products/<int:pk>/review/', ProductReviewCreateAPIView.as_view(), name='product-review'),
    path('products/popular/',ProductsPopularAPIView.as_view(), name='products-popular'),
    path('products/limited/',ProductsLimitedAPIView.as_view(), name='products-limited'),
    path('sales/', SaleItemListAPIView.as_view(), name='sales'),
    path('tags/', ProductTagListAPIView.as_view(), name='tags'),
    path('banners/', BannerListAPIView.as_view(), name='banners'),
]
