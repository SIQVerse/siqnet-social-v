from django import forms
from .models import CivicPost

class CivicPostForm(forms.ModelForm):
    class Meta:
        model = CivicPost
        fields = [
            'title',
            'content',
            'image',
            'video',
            'audio',
            'tags',
            'visibility',
            'post_type',
            'location',
        ]
        widgets = {
            'tags': forms.TextInput(attrs={'placeholder': 'e.g. #tech, #education'}),
            'location': forms.TextInput(attrs={'placeholder': 'City, Region or GPS'}),
            'visibility': forms.Select(),
            'post_type': forms.Select(),
        }
