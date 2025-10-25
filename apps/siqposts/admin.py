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

    @admin.action(description="Hide selected posts")
    def hide_posts(self, request, queryset):
        queryset.update(is_hidden=True)

    @admin.action(description="Unhide selected posts")
    def unhide_posts(self, request, queryset):
        queryset.update(is_hidden=False)

    @admin.action(description="Flag selected posts")
    def flag_posts(self, request, queryset):
        queryset.update(is_flagged=True)

    @admin.action(description="Unflag selected posts")
    def unflag_posts(self, request, queryset):
        queryset.update(is_flagged=False)


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

    @admin.action(description="Hide selected comments")
    def hide_comments(self, request, queryset):
        queryset.update(is_hidden=True)

    @admin.action(description="Unhide selected comments")
    def unhide_comments(self, request, queryset):
        queryset.update(is_hidden=False)

    @admin.action(description="Flag selected comments")
    def flag_comments(self, request, queryset):
        queryset.update(is_flagged=True)

    @admin.action(description="Unflag selected comments")
    def unflag_comments(self, request, queryset):
        queryset.update(is_flagged=False)
