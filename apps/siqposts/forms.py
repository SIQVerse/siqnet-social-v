from django import forms
from .models import CivicPost

class CivicPostForm(forms.ModelForm):
    class Meta:
        model = CivicPost
        fields = ['title', 'content', 'image']
