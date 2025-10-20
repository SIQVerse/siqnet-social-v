from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import CivicPost
from .forms import CivicPostForm

@login_required
def post_list_view(request):
    posts = CivicPost.objects.all().order_by('-created_at')
    return render(request, 'siqposts/post_list.html', {'posts': posts})

@login_required
def post_detail_view(request, post_id):
    post = get_object_or_404(CivicPost, id=post_id)
    return render(request, 'siqposts/post_detail.html', {'post': post})

@login_required
def post_create_view(request):
    if request.method == 'POST':
        form = CivicPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = CivicPostForm()
    return render(request, 'siqposts/post_form.html', {'form': form, 'action': 'Create'})

@login_required
def post_edit_view(request, post_id):
    post = get_object_or_404(CivicPost, id=post_id)
    if post.author != request.user:
        return redirect('post_detail', post_id=post.id)
    if request.method == 'POST':
        form = CivicPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = CivicPostForm(instance=post)
    return render(request, 'siqposts/post_form.html', {'form': form, 'action': 'Edit'})
