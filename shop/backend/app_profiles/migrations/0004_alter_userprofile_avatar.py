# Generated by Django 4.1.7 on 2023-04-12 16:32

import app_profiles.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_profiles', '0003_alter_userprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(null=True, upload_to=app_profiles.models.profile_avatar_directory_path, verbose_name='avatar'),
        ),
    ]