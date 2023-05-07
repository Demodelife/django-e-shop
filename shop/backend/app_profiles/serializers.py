from django.contrib.auth.models import User
from rest_framework import serializers
from app_profiles.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    """
    Сериализатор профиля пользователя
    """

    class Meta:
        model = UserProfile
        fields = (
            'fullName',
            'phone',
            'avatar',
            'email'
        )
        read_only_fields = 'avatar',


class UserProfileAvatarUpdateSerializer(serializers.ModelSerializer):
    """
    Сериализатор обновления аватара пользователя
    """

    class Meta:
        model = UserProfile
        fields = 'avatar',


class UserProfilePasswordUpdateSerializer(serializers.ModelSerializer):
    """
    Сериализатор обновления пароля пользователя
    """
    passwordCurrent = serializers.CharField(required=True, write_only=True)
    passwordReply = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = (
            'passwordCurrent',
            'password',
            'passwordReply',
        )


    def validate(self, data):
        user = self.context['request'].user

        if not user.check_password(data.get('passwordCurrent')):
            raise serializers.ValidationError('Incorrect old password')

        return data
