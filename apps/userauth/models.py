from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)

    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)

    is_verified = models.BooleanField(default=False)
    badge = models.CharField(max_length=50, blank=True)
    reputation_score = models.IntegerField(default=0)
    last_seen = models.DateTimeField(null=True, blank=True)
    is_online = models.BooleanField(default=False)

    allow_messages = models.BooleanField(default=True)
    allow_tags = models.BooleanField(default=True)
    role = models.CharField(max_length=20, choices=[
        ('user', 'User'),
        ('creator', 'Creator'),
        ('moderator', 'Moderator'),
        ('admin', 'Admin'),
    ], default='user')

    groups = models.ManyToManyField('auth.Group', related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='customuser_set', blank=True)

    def __str__(self):
        return self.username

    def total_followers(self):
        return self.followers.count()

    def total_following(self):
        return self.following.count()


class CivicPost(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='civic_posts')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.author.username}: {self.content[:30]}"
