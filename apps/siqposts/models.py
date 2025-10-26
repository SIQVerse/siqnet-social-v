from django.db import models
from django.conf import settings

class CivicPost(models.Model):
    """
    Represents a civic engagement post which can be text, image, video, poll, or audio.
    """

    POST_TYPES = [
        ('text', 'Text'),
        ('image', 'Image'),
        ('video', 'Video'),
        ('poll', 'Poll'),
        ('audio', 'Audio'),
    ]

    VISIBILITY_CHOICES = [
        ('public', 'Public'),
        ('private', 'Private'),
        ('friends', 'Friends Only'),
        ('group', 'Group Only'),
    ]

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='posts/images/', blank=True, null=True)
    video = models.FileField(upload_to='posts/videos/', blank=True, null=True)
    audio = models.FileField(upload_to='posts/audio/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='liked_posts',
        blank=True
    )
    views = models.PositiveIntegerField(default=0)
    shares = models.PositiveIntegerField(default=0)
    tags = models.CharField(max_length=200, blank=True)  # comma-separated hashtags
    visibility = models.CharField(max_length=10, choices=VISIBILITY_CHOICES, default='public')
    post_type = models.CharField(max_length=10, choices=POST_TYPES, default='text')
    location = models.CharField(max_length=100, blank=True)

    is_flagged = models.BooleanField(default=False)
    is_hidden = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} by {self.author.username}"

    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    """
    Represents a comment on a CivicPost, with support for threaded replies.
    """

    post = models.ForeignKey(CivicPost, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='replies'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='liked_comments',
        blank=True
    )
    is_edited = models.BooleanField(default=False)
    is_flagged = models.BooleanField(default=False)
    is_hidden = models.BooleanField(default=False)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"

    def is_reply(self):
        return self.parent is not None

    def total_likes(self):
        return self.likes.count()


class Poll(models.Model):
    """
    Represents a poll attached to a CivicPost.
    """

    post = models.OneToOneField(CivicPost, on_delete=models.CASCADE, related_name='poll')
    question = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Poll: {self.question}"


class PollOption(models.Model):
    """
    Represents an option within a poll.
    """

    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='options')
    text = models.CharField(max_length=100)
    votes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

    def __str__(self):
        return self.text

    def vote_count(self):
        return self.votes.count()
