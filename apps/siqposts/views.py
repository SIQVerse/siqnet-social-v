from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import CivicPost, Comment
from .forms import CivicPostForm, CommentForm

@login_required
def post_list_view(request):
    posts = CivicPost.objects.filter(is_hidden=False).order_by('-created_at')
    return render(request, 'siqposts/post_list.html', {'posts': posts})

@login_required
def post_detail_view(request, post_id):
    post = get_object_or_404(CivicPost, id=post_id)
    post.views += 1
    post.save()
    comments = post.comments.filter(is_hidden=False).order_by('created_at')
    return render(request, 'siqposts/post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': CommentForm()
    })

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

@login_required
def post_delete_view(request, post_id):
    post = get_object_or_404(CivicPost, id=post_id)
    if post.author != request.user:
        return redirect('post_detail', post_id=post.id)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'siqposts/post_confirm_delete.html', {'post': post})

@login_required
def post_like_view(request, post_id):
    post = get_object_or_404(CivicPost, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return JsonResponse({'likes': post.total_likes()})

@login_required
def post_share_view(request, post_id):
    post = get_object_or_404(CivicPost, id=post_id)
    post.shares += 1
    post.save()
    return JsonResponse({'shares': post.shares})

@login_required
def comment_create_view(request, post_id):
    post = get_object_or_404(CivicPost, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', post_id=post.id)
    return redirect('post_detail', post_id=post.id)

@login_required
def comment_reply_view(request, comment_id):
    parent = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.author = request.user
            reply.post = parent.post
            reply.parent = parent
            reply.save()
            return redirect('post_detail', post_id=parent.post.id)
    return redirect('post_detail', post_id=parent.post.id)

@login_required
def comment_like_view(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user in comment.likes.all():
        comment.likes.remove(request.user)
    else:
        comment.likes.add(request.user)
    return JsonResponse({'likes': comment.total_likes()})
