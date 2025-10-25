from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from .models import CivicPost

User = get_user_model()

def register_view(request):
    """
    Placeholder view for user registration.
    """
    return HttpResponse("Register page coming soon.")

def login_view(request):
    """
    Placeholder view for user login.
    """
    return HttpResponse("Login page coming soon.")

def logout_view(request):
    """
    Placeholder view for user logout.
    """
    return HttpResponse("Logout page coming soon.")

def profile_view(request, username):
    """
    Display the public profile of a user along with their civic posts.
    """
    profile_user = get_object_or_404(User, username=username)
    civic_posts = CivicPost.objects.filter(author=profile_user).order_by('-created_at')

    context = {
        'profile_user': profile_user,
        'posts': civic_posts,
        'is_own_profile': request.user == profile_user,
    }

    return render(request, 'userauth/profile.html', context)
