from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import CivicPost, Comment

User = get_user_model()

class CivicPostTestCase(TestCase):
    """✅ Tests for CivicPost model behavior."""

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass')
        self.post = CivicPost.objects.create(
            author=self.user,
            title='Test Post',
            content='This is a test post.'
        )

    def test_post_creation(self):
        """Ensure a post is created with correct title and author."""
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.author.username, 'testuser')
        self.assertTrue(isinstance(self.post, CivicPost))
        self.assertEqual(str(self.post), f"{self.post.title} by {self.post.author.username}")

class CommentTestCase(TestCase):
    """✅ Tests for Comment model behavior."""

    def setUp(self):
        self.user = User.objects.create_user(username='commenter', password='pass')
        self.post = CivicPost.objects.create(
            author=self.user,
            title='Another Post',
            content='Post content here.'
        )
        self.comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            content='Nice!'
        )

    def test_comment_linked_to_post(self):
        """Ensure comment is correctly linked to its post."""
        self.assertEqual(self.comment.post.title, 'Another Post')
        self.assertEqual(self.comment.author.username, 'commenter')
        self.assertTrue(isinstance(self.comment, Comment))
        self.assertEqual(str(self.comment), f"Comment by {self.comment.author.username} on {self.comment.post.title}")
