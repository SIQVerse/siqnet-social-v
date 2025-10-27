from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CivicPost, Comment
from apps.notifications.models import Notification

# 📢 Notify author when a new post is created
@receiver(post_save, sender=CivicPost)
def notify_new_post(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            recipient=instance.author,
            message=f"Your post '{instance.title}' was published successfully.",
            type='post_created'
        )

# 💬 Notify post author when someone comments
@receiver(post_save, sender=Comment)
def notify_new_comment(sender, instance, created, **kwargs):
    if created and instance.post.author != instance.author:
        Notification.objects.create(
            recipient=instance.post.author,
            message=f"{instance.author.username} commented on your post '{instance.post.title}'.",
            type='comment_received'
        )
