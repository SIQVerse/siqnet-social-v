from django.contrib import admin
from .models import CivicPost

@admin.register(CivicPost)
class CivicPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'content', 'author__username')
    list_filter = ('created_at',)
