from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import render

from rest_framework import status
from rest_framework.generics import GenericAPIView, get_object_or_404, RetrieveAPIView, ListCreateAPIView, \
    RetrieveUpdateAPIView
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from app_profiles.models import UserProfile
from app_profiles.serializers import UserProfileSerializer


# class UserProfileDetailAPIView(RetrieveAPIView):
#     """Представление профиля пользователя"""
#     serializer_class = UserProfileSerializer
#     queryset = UserProfile.objects.all()
#
#     def get_object(self):
#         return self.request.user.profile

# class UserProfileListAPIView(ListCreateAPIView):
#     queryset = UserProfile.objects.all()
#     serializer_class = UserProfileSerializer
#
#     def get_serializer_class(self):
#         if self.request.method == 'POST':
#             return UserProfileCreateSerializer
#         return UserProfileSerializer

class UserProfileAPIView(RetrieveUpdateAPIView):
    """
    Представление для получения и обновления информации профиля
    """
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.profile