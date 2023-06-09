from django.contrib import admin
from app_profiles.models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = 'id', 'user', 'fullName', 'email', 'phone'
    list_display_links = 'id', 'fullName'


