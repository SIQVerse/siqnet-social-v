from django import forms
from .models import CivicPost, Comment

class CivicPostForm(forms.ModelForm):
    content = forms.CharField(
        label="What's happening?",
        widget=forms.Textarea(attrs={
            'rows': 4,
            'placeholder': 'Share your civic thoughts...',
            'class': 'form-control'
        })
    )

    class Meta:
        model = CivicPost
        fields = ['content']

class CommentForm(forms.ModelForm):
    text = forms.CharField(
        label="Add a comment",
        widget=forms.Textarea(attrs={
            'rows': 2,
            'placeholder': 'Write your comment...',
            'class': 'form-control'
        })
    )

    class Meta:
        model = Comment
        fields = ['text']
