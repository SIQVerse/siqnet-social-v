from django.contrib.auth import get_user_model
from django.shortcuts import render
from .models import CivicPost  # Assuming CivicPost is defined in models.py

User = get_user_model()

def profile_view(request, username):
    user = User.objects.get(username=username)
    return render(request, 'userauth/profile.html', {'user': user})
