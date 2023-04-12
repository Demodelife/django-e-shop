from django.contrib.auth import get_user_model
from rest_framework import serializers
from app_profiles.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    """Сериализатор профиля пользователя"""

    class Meta:
        model = UserProfile
        fields = ('fullName', 'phone', 'avatar', 'email')
        read_only_fields = 'avatar',


