from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, VerificationRequest

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['profile_picture', 'location', 'bio']

class VerificationRequestForm(forms.ModelForm):
    class Meta:
        model = VerificationRequest
        fields = ['notes']
