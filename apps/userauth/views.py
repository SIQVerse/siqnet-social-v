from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from .models import CivicPost

User = get_user_model()

# 🔐 Authentication
def register_view(request):
    return HttpResponse("Register page coming soon.")

def login_view(request):
    return HttpResponse("Login page coming soon.")

def logout_view(request):
    return HttpResponse("Logout page coming soon.")

# 👤 Profile & Identity
def profile_view(request):
    return HttpResponse("Current user's profile page coming soon.")

def profile_edit_view(request):
    return HttpResponse("Profile edit page coming soon.")

def public_profile_view(request, username):
    profile_user = get_object_or_404(User, username=username)
    civic_posts = CivicPost.objects.filter(author=profile_user).order_by('-created_at')

    context = {
        'profile_user': profile_user,
        'posts': civic_posts,
        'is_own_profile': request.user == profile_user,
    }

    return render(request, 'userauth/profile.html', context)

# ⚙️ Account Settings
def account_settings_view(request):
    return HttpResponse("Account settings page coming soon.")

def security_settings_view(request):
    return HttpResponse("Security settings page coming soon.")

# 🏅 Verification & Badges
def verification_request_view(request):
    return HttpResponse("Verification request page coming soon.")

def user_badges_view(request):
    return HttpResponse("User badges page coming soon.")

# 📊 Activity & Analytics
def user_activity_view(request):
    return HttpResponse("User activity page coming soon.")
