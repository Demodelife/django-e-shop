from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _



def profile_avatar_directory_path(instance: 'UserProfile', filename: str) -> str:
    return 'profiles/profile_{pk}/avatar/{filename}'.format(
        pk=instance.user.pk,
        filename=filename,
    )

class UserProfile(models.Model):
    """Модель профиля пользователя"""
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE, verbose_name=_('user'))
    fullName = models.CharField(max_length=255, verbose_name=_('full name'))
    phone = models.CharField(max_length=20, verbose_name=_('phone'))
    email = models.EmailField(unique=True, null=True, verbose_name=_('email'))
    avatar = models.ImageField(null=True, upload_to=profile_avatar_directory_path, verbose_name=_('avatar'))

    class Meta:
        verbose_name_plural = _('profiles')
        verbose_name = _('profile')

    def __str__(self):
        return f'User {self.fullName}'