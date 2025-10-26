from django.contrib import admin
from .models import CustomUser, CivicPost, Badge, UserBadge, VerificationRequest, UserActivity
from django.contrib.auth.admin import UserAdmin

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('profile_picture', 'location', 'bio', 'is_verified')}),
    )

admin.site.register(CivicPost)
admin.site.register(Badge)
admin.site.register(UserBadge)
admin.site.register(VerificationRequest)
admin.site.register(UserActivity)
