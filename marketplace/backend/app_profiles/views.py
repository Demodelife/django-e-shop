from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import render

from rest_framework import status
from rest_framework.generics import GenericAPIView, get_object_or_404, RetrieveAPIView, ListCreateAPIView, \
    RetrieveUpdateAPIView, UpdateAPIView
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from app_profiles.models import UserProfile
from app_profiles.serializers import UserProfileSerializer, UserProfileAvatarUpdateSerializer, \
    UserProfilePasswordUpdateSerializer


# class UserProfileAPIView(APIView):
#     """
#     Представление для получения и обновления информации профиля
#     """
#     serializer_class = UserProfileSerializer
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request, *args, **kwargs):
#         profile = self.request.user.profile
#         serializer = self.serializer_class(profile)
#         return Response(serializer.data)
#
#     def post(self, request, *args, **kwargs):
#         profile = self.request.user.profile
#         serializer = self.serializer_class(profile, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserProfileAPIView(RetrieveUpdateAPIView):
    """
    Представление для получения и обновления информации профиля
    """
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.profile


class UserProfileAvatarUpdateAPIView(RetrieveUpdateAPIView):
    """
    Представление для обновления аватара пользователя
    """
    serializer_class = UserProfileAvatarUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.profile


class UserProfilePasswordUpdateAPIView(RetrieveUpdateAPIView):
    """
    Представление для обновления пароля пользователя
    """
    serializer_class = UserProfilePasswordUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
