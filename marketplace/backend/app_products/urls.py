from django.urls import path

from app_products.views import (
    CategoryListAPIView,
    ProductListAPIView,
    ProductDetailAPIView, SaleItemListAPIView
)



app_name = 'app_products'


urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='categories'),
    path('catalog/', ProductListAPIView.as_view(), name='catalog'),
    # path('catalog/<int:pk>/', ProductDetailAPIView.as_view(), name='catalog-detail'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('sales/', SaleItemListAPIView.as_view(), name='sales'),
]
