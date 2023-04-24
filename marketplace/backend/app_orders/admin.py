from django.contrib import admin

from app_orders.models import Order, OrderProduct, Payment


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = 'id', 'fullName', 'email', 'totalCost', 'address', 'createdAt', 'payment', 'status'


@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = 'id', 'order', 'product'


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = 'id', 'order', 'name'
