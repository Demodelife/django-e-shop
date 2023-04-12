from django.urls import path

from app_profiles.views import UserProfileAPIView

app_name = 'app_profiles'


urlpatterns = [
    path('profile/', UserProfileAPIView.as_view(), name='profile')
]