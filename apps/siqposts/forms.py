from django import forms
from .models import CivicPost, Comment

class CivicPostForm(forms.ModelForm):
    content = forms.CharField(
        label="What's happening?",
        widget=forms.Textarea(attrs={
            'rows': 4,
            'placeholder': 'Share your civic thoughts...',
            'class': 'form-control'
        }),
        required=False
    )

    image = forms.ImageField(required=False)
    video = forms.FileField(required=False)
    audio = forms.FileField(required=False)
    tags = forms.CharField(required=False)
    visibility = forms.ChoiceField(choices=CivicPost.VISIBILITY_CHOICES, required=False)
    post_type = forms.ChoiceField(choices=CivicPost.POST_TYPES, required=False)

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
