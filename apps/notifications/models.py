from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class Notification(models.Model):
    """
    Represents a system or user-generated notification sent to a recipient.
    """
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)
    link = models.URLField(blank=True, null=True)  # Optional: link to related content

    def __str__(self):
        return f"Notification for {self.recipient.username} - {'Read' if self.is_read else 'Unread'}"
