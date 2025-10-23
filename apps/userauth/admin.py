from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser

    fieldsets = UserAdmin.fieldsets + (
        ("Profile Info", {
            'fields': (
                'bio',
                'location',
                'profile_picture',
                'badge',
                'is_verified',
                'reputation_score',
                'last_seen',
                'is_online',
            )
        }),
        ("Social & Privacy", {
            'fields': (
                'followers',
                'allow_messages',
                'allow_tags',
                'role',
            )
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Profile Info", {
            'fields': (
                'bio',
                'location',
                'profile_picture',
                'badge',
                'is_verified',
                'reputation_score',
                'last_seen',
                'is_online',
            )
        }),
        ("Social & Privacy", {
            'fields': (
                'followers',
                'allow_messages',
                'allow_tags',
                'role',
            )
        }),
    )

    list_display = (
        'username',
        'email',
        'role',
        'is_verified',
        'reputation_score',
        'is_online',
        'last_login',
        'date_joined',
    )
    search_fields = (
        'username',
        'email',
        'location',
        'badge',
    )
