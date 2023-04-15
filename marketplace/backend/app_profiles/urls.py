from django.urls import path

from app_profiles.views import (
    UserProfileAPIView,
    UserProfileAvatarUpdateAPIView,
    UserProfilePasswordUpdateAPIView
)

app_name = 'app_profiles'


urlpatterns = [
    path('profile/', UserProfileAPIView.as_view(), name='profile'),
    path('profile/avatar/', UserProfileAvatarUpdateAPIView.as_view(), name='profile-avatar'),
    path('profile/password/', UserProfilePasswordUpdateAPIView.as_view(), name='profile-password'),
]