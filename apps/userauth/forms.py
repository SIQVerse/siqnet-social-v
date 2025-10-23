from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(
        choices=[
            ('user', 'User'),
            ('creator', 'Creator'),
            ('moderator', 'Moderator'),
        ],
        help_text="Choose your role on SIQNet"
    )
    allow_messages = forms.BooleanField(required=False, initial=True, label="Allow direct messages")
    allow_tags = forms.BooleanField(required=False, initial=True, label="Allow others to tag you")

    class Meta:
        model = CustomUser
        fields = [
            'username',
            'email',
            'password1',
            'password2',
            'bio',
            'location',
            'profile_picture',
            'role',
            'allow_messages',
            'allow_tags',
        ]


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username or Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'bio',
            'location',
            'profile_picture',
            'role',
            'allow_messages',
            'allow_tags',
        ]
