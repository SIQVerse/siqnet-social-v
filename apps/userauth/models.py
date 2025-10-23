from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)

    # Social Graph
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)

    # Status & Identity
    is_verified = models.BooleanField(default=False)
    badge = models.CharField(max_length=50, blank=True)  # e.g. "Educator", "Influencer", "Moderator"
    reputation_score = models.IntegerField(default=0)
    last_seen = models.DateTimeField(null=True, blank=True)
    is_online = models.BooleanField(default=False)

    # Privacy & Roles
    allow_messages = models.BooleanField(default=True)
    allow_tags = models.BooleanField(default=True)
    role = models.CharField(max_length=20, choices=[
        ('user', 'User'),
        ('creator', 'Creator'),
        ('moderator', 'Moderator'),
        ('admin', 'Admin'),
    ], default='user')

    # Permissions
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True
    )

    def __str__(self):
        return self.username

    def total_followers(self):
        return self.followers.count()

    def total_following(self):
        return self.following.count()
