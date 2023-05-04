from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from app_profiles.serializers import (
    UserProfileSerializer,
    UserProfileAvatarUpdateSerializer,
    UserProfilePasswordUpdateSerializer,
)


class UserProfileAPIView(GenericAPIView):
    """
    Представление для получения и обновления информации профиля.
    """
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]


    def get(self, request: Request, *args, **kwargs) -> Response:
        profile = self.request.user.profile
        serializer = self.serializer_class(profile)
        return Response(serializer.data)


    def post(self, request: Request, *args, **kwargs) -> Response:
        profile = self.request.user.profile
        serializer = self.serializer_class(profile, data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfilePasswordUpdateAPIView(GenericAPIView):
    """
    Представление для обновления пароля пользователя.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = UserProfilePasswordUpdateSerializer(
            data=self.request.data,
            context={'request': self.request}
        )
        if serializer.is_valid():
            user = self.request.user
            user.set_password(serializer.validated_data['password'])
            user.save()
            return Response({'detail': 'Password changed successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileAvatarUpdateAPIView(GenericAPIView):
    """
    Представление для обновления аватара пользователя.
    """
    serializer_class = UserProfileAvatarUpdateSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request: Request, *args, **kwargs) -> Response:
        profile = self.request.user.profile
        serializer = self.serializer_class(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Avatar changed successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)