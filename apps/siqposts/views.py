from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CivicPost

@login_required
def post_list_view(request):
    posts = CivicPost.objects.all().order_by('-created_at')
    return render(request, 'siqposts/post_list.html', {'posts': posts})

@login_required
def post_detail_view(request, post_id):
    post = get_object_or_404(CivicPost, id=post_id)
    return render(request, 'siqposts/post_detail.html', {'post': post})
