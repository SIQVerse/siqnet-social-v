from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# 👤 Custom User Model
class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    location = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username

# 📝 Civic Post Model
class CivicPost(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='civic_posts')
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Post by {self.author.username} on {self.created_at.strftime('%Y-%m-%d %H:%M')}"

# 🏅 Badge Model
class Badge(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    icon = models.ImageField(upload_to='badges/', blank=True, null=True)

    def __str__(self):
        return self.name

# 🧑‍🎓 User Badge Assignment
class UserBadge(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='badges')
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    awarded_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} - {self.badge.name}"

# ✅ Verification Request
class VerificationRequest(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], default='pending')
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.status}"

# 📊 User Activity Log
class UserActivity(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    action = models.CharField(max_length=100)
    timestamp = models.DateTimeField(default=timezone.now)
    metadata = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.action} @ {self.timestamp.strftime('%Y-%m-%d %H:%M')}"
