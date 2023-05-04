from django.urls import path

from app_cart.views import CartAPIView

app_name = 'app_cart'


urlpatterns = [
    path('basket/', CartAPIView.as_view(), name='cart'),
]