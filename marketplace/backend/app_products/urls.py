from django.urls import path

from app_products.views import CategoryListAPIView, ProductListAPIView

app_name = 'app_products'


urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('products/', ProductListAPIView.as_view(), name='product-list'),
]
