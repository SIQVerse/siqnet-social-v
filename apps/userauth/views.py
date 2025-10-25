from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm, ProfileEditForm, VerificationRequestForm
from .models import CustomUser, CivicPost, UserBadge, UserActivity, VerificationRequest

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
            login(request, form.get_user())
            return redirect('profile')
    else:
        form = LoginForm()
    return render(request, 'userauth/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile_view(request):
    posts = CivicPost.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'userauth/profile.html', {
        'profile_user': request.user,
        'posts': posts,
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
    profile_user = get_object_or_404(CustomUser, username=username)
    posts = CivicPost.objects.filter(author=profile_user).order_by('-created_at')
    return render(request, 'userauth/profile.html', {
        'profile_user': profile_user,
        'posts': posts,
        'is_own_profile': request.user == profile_user,
    })

@login_required
def account_settings_view(request):
    return render(request, 'userauth/settings.html')

@login_required
def security_settings_view(request):
    return render(request, 'userauth/security_settings.html')

@login_required
def verification_request_view(request):
    if request.method == 'POST':
        form = VerificationRequestForm(request.POST)
        if form.is_valid():
            VerificationRequest.objects.create(user=request.user, notes=form.cleaned_data['notes'])
            return redirect('profile')
    else:
        form = VerificationRequestForm()
    return render(request, 'userauth/verification_request.html', {'form': form})

@login_required
def user_badges_view(request):
    badges = UserBadge.objects.filter(user=request.user).select_related('badge')
    return render(request, 'userauth/badges.html', {'badges': badges})

@login_required
def user_activity_view(request):
    activities = UserActivity.objects.filter(user=request.user).order_by('-timestamp')[:50]
    return render(request, 'userauth/activity.html', {'activities': activities})
