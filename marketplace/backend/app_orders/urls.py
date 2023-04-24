from django.urls import path
from app_orders.views import (
    OrderActiveAPIView,
    OrderConfirmRetrieveAPIView,
    OrderListCreateAPIView,
    PaymentAPIView,
)


app_name = 'app_orders'



urlpatterns = [
    path('orders/', OrderListCreateAPIView.as_view(), name='orders-list-create'),
    path('orders/active/', OrderActiveAPIView.as_view(), name='order-active'),
    path('orders/<int:pk>/', OrderConfirmRetrieveAPIView.as_view(), name='order-confirm-retrieve'),
    path('payment/', PaymentAPIView.as_view(), name='payment'),
]