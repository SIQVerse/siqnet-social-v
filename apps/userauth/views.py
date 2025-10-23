from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, UserLoginForm, ProfileUpdateForm
from .models import UserProfile, CivicPost

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)  # Create profile automatically
            login(request, user)
            messages.success(request, "Welcome to SIQNet!")
            return redirect('profile')
    else:
        form = UserRegistrationForm()
    return render(request, 'userauth/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, "Login successful.")
            return redirect('profile')
    else:
        form = UserLoginForm()
    return render(request, 'userauth/login.html', {'form': form})

@login_required
def profile_view(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    posts = CivicPost.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'userauth/profile.html', {
        'user': request.user,
        'profile': profile,
        'posts': posts,
    })

@login_required
def profile_edit_view(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated.")
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=profile)
    return render(request, 'userauth/profile_edit.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "You’ve been logged out.")
    return redirect('login')
