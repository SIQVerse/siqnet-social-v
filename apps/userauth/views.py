from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm, ProfileEditForm
from .models import User, CivicPost

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = RegisterForm()
    return render(request, 'userauth/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = LoginForm()
    return render(request, 'userauth/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile_view(request):
    civic_posts = CivicPost.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'userauth/profile.html', {
        'profile_user': request.user,
        'posts': civic_posts,
        'is_own_profile': True,
    })

@login_required
def profile_edit_view(request):
    form = ProfileEditForm(instance=request.user)
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    return render(request, 'userauth/profile_edit.html', {'form': form})

def public_profile_view(request, username):
    profile_user = get_object_or_404(User, username=username)
    civic_posts = CivicPost.objects.filter(author=profile_user).order_by('-created_at')
    return render(request, 'userauth/profile.html', {
        'profile_user': profile_user,
        'posts': civic_posts,
        'is_own_profile': request.user == profile_user,
    })
