from django.contrib import admin
from .models import CivicPost, Comment

@admin.register(CivicPost)
class CivicPostAdmin(admin.ModelAdmin):
    """
    Admin interface for CivicPost model with custom actions and display fields.
    """

    list_display = (
        'title',
        'author',
        'post_type',
        'visibility',
        'created_at',
        'updated_at',
        'display_total_likes',
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
    readonly_fields = ('views', 'shares', 'display_total_likes')
    actions = ['hide_posts', 'unhide_posts', 'flag_posts', 'unflag_posts']

    @admin.display(description="Total Likes")
    def display_total_likes(self, obj):
        return obj.total_likes()

    @admin.action(description="Hide selected posts")
    def hide_posts(self, request, queryset):
        updated = queryset.update(is_hidden=True)
        self.message_user(request, f"{updated} post(s) hidden.")

    @admin.action(description="Unhide selected posts")
    def unhide_posts(self, request, queryset):
        updated = queryset.update(is_hidden=False)
        self.message_user(request, f"{updated} post(s) unhidden.")

    @admin.action(description="Flag selected posts")
    def flag_posts(self, request, queryset):
        updated = queryset.update(is_flagged=True)
        self.message_user(request, f"{updated} post(s) flagged.")

    @admin.action(description="Unflag selected posts")
    def unflag_posts(self, request, queryset):
        updated = queryset.update(is_flagged=False)
        self.message_user(request, f"{updated} post(s) unflagged.")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Admin interface for Comment model with moderation actions and reply detection.
    """

    list_display = (
        'author',
        'post',
        'created_at',
        'updated_at',
        'display_is_reply',
        'display_total_likes',
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

    @admin.display(description="Is Reply")
    def display_is_reply(self, obj):
        return obj.is_reply()

    @admin.display(description="Total Likes")
    def display_total_likes(self, obj):
        return obj.total_likes()

    @admin.action(description="Hide selected comments")
    def hide_comments(self, request, queryset):
        updated = queryset.update(is_hidden=True)
        self.message_user(request, f"{updated} comment(s) hidden.")

    @admin.action(description="Unhide selected comments")
    def unhide_comments(self, request, queryset):
        updated = queryset.update(is_hidden=False)
        self.message_user(request, f"{updated} comment(s) unhidden.")

    @admin.action(description="Flag selected comments")
    def flag_comments(self, request, queryset):
        updated = queryset.update(is_flagged=True)
        self.message_user(request, f"{updated} comment(s) flagged.")

    @admin.action(description="Unflag selected comments")
    def unflag_comments(self, request, queryset):
        updated = queryset.update(is_flagged=False)
        self.message_user(request, f"{updated} comment(s) unflagged.")
