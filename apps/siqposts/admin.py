from django.contrib import admin
from .models import CivicPost, Comment

@admin.register(CivicPost)
class CivicPostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'post_type',
        'visibility',
        'created_at',
        'updated_at',
        'total_likes',
        'views',
        'shares',
        'is_flagged',
        'is_hidden',
    )
    search_fields = (
        'title',
        'content',
        'tags',
        'location',
        'author__username',
    )
    list_filter = (
        'created_at',
        'updated_at',
        'visibility',
        'post_type',
        'is_flagged',
        'is_hidden',
    )
    readonly_fields = ('views', 'shares', 'total_likes')
    actions = ['hide_posts', 'unhide_posts', 'flag_posts', 'unflag_posts']

    def hide_posts(self, request, queryset):
        queryset.update(is_hidden=True)
    hide_posts.short_description = "Hide selected posts"

    def unhide_posts(self, request, queryset):
        queryset.update(is_hidden=False)
    unhide_posts.short_description = "Unhide selected posts"

    def flag_posts(self, request, queryset):
        queryset.update(is_flagged=True)
    flag_posts.short_description = "Flag selected posts"

    def unflag_posts(self, request, queryset):
        queryset.update(is_flagged=False)
    unflag_posts.short_description = "Unflag selected posts"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'post',
        'created_at',
        'updated_at',
        'is_reply',
        'total_likes',
        'is_flagged',
        'is_hidden',
    )
    search_fields = (
        'content',
        'author__username',
        'post__title',
    )
    list_filter = (
        'created_at',
        'updated_at',
        'is_flagged',
        'is_hidden',
    )
    actions = ['hide_comments', 'unhide_comments', 'flag_comments', 'unflag_comments']

    def hide_comments(self, request, queryset):
        queryset.update(is_hidden=True)
    hide_comments.short_description = "Hide selected comments"

    def unhide_comments(self, request, queryset):
        queryset.update(is_hidden=False)
    unhide_comments.short_description = "Unhide selected comments"

    def flag_comments(self, request, queryset):
        queryset.update(is_flagged=True)
    flag_comments.short_description = "Flag selected comments"

    def unflag_comments(self, request, queryset):
        queryset.update(is_flagged=False)
    unflag_comments.short_description = "Unflag selected comments"
