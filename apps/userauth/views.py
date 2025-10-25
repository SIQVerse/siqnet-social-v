from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from .models import CivicPost

User = get_user_model()

def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    posts = CivicPost.objects.filter(author=user).order_by('-created_at')
    return render(request, 'userauth/profile.html', {
        'user': user,
        'posts': posts
    })
