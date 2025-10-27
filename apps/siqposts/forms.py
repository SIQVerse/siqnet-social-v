from django import forms
from .models import CivicPost, Comment

# 📝 CivicPost Form for creating/editing posts
class CivicPostForm(forms.ModelForm):
    content = forms.CharField(
        label="What's happening?",
        required=False,
        widget=forms.Textarea(attrs={
            'rows': 4,
            'placeholder': 'Share your civic thoughts...',
            'class': 'form-control'
        })
    )

    image = forms.ImageField(
        label="Upload an image",
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )

    video = forms.FileField(
        label="Attach a video",
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )

    audio = forms.FileField(
        label="Attach audio",
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )

    tags = forms.CharField(
        label="Tags",
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'e.g. environment, policy'
        })
    )

    visibility = forms.ChoiceField(
        label="Visibility",
        choices=CivicPost.VISIBILITY_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    post_type = forms.ChoiceField(
        label="Post Type",
        choices=CivicPost.POST_TYPES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

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
            'location'
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Post title'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'City, region, or coordinates'
            }),
        }

# 💬 Comment Form for adding/editing comments
class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label="Add a comment",
        widget=forms.Textarea(attrs={
            'rows': 2,
            'placeholder': 'Write your comment...',
            'class': 'form-control'
        })
    )

    class Meta:
        model = Comment
        fields = ['content']
