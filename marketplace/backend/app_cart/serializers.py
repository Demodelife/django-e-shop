from rest_framework import serializers


class CartItemSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    count = serializers.IntegerField()