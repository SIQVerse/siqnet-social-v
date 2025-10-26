from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import CivicPost, Comment, Poll, PollOption
from .forms import CivicPostForm, CommentForm
from .serializers import CivicPostSerializer, CommentSerializer

# 🌐 DRF ViewSets
class CivicPostViewSet(viewsets.ModelViewSet):
    queryset = CivicPost.objects.all().order_by('-created_at')
    serializer_class = CivicPostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        post = self.get_object()
        user = request.user
        if user in post.likes.all():
            post.likes.remove(user)
            return Response({'status': 'unliked'})
        else:
            post.likes.add(user)
            return Response({'status': 'liked'})

    @action(detail=True, methods=['post'])
    def view(self, request, pk=None):
        post = self.get_object()
        post.views += 1
        post.save()
        return Response({'views': post.views})


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        comment = self.get_object()
        user = request.user
        if user in comment.likes.all():
            comment.likes.remove(user)
            return Response({'status': 'unliked'})
        else:
            comment.likes.add(user)
            return Response({'status': 'liked'})


# 📝 Django Views
def post_list_view(request):
    posts = CivicPost.objects.all().order_by('-created_at')
    return render(request, 'siqposts/post_list.html', {'posts': posts})


def post_detail_view(request, post_id):
    post = get_object_or_404(CivicPost, id=post_id)
    comments = post.comments.all().order_by('-created_at')
    return render(request, 'siqposts/post_detail.html', {'post': post, 'comments': comments})


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
    return render(request, 'siqposts/create_post.html', {'form': form})


def post_edit_view(request, post_id):
    post = get_object_or_404(CivicPost, id=post_id)
    if request.method == 'POST':
        form = CivicPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = CivicPostForm(instance=post)
    return render(request, 'siqposts/edit_post.html', {'form': form, 'post': post})


def post_delete_view(request, post_id):
    post = get_object_or_404(CivicPost, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'siqposts/delete_post.html', {'post': post})


def post_like_view(request, post_id):
    post = get_object_or_404(CivicPost, id=post_id)
    user = request.user
    if user in post.likes.all():
        post.likes.remove(user)
    else:
        post.likes.add(user)
    return JsonResponse({'likes': post.likes.count()})


def post_share_view(request, post_id):
    post = get_object_or_404(CivicPost, id=post_id)
    post.shares += 1
    post.save()
    return JsonResponse({'shares': post.shares})


def post_view_tracker(request, post_id):
    post = get_object_or_404(CivicPost, id=post_id)
    post.views += 1
    post.save()
    return JsonResponse({'views': post.views})


def comment_create_view(request, post_id):
    post = get_object_or_404(CivicPost, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = CommentForm()
    return render(request, 'siqposts/create_comment.html', {'form': form, 'post': post})


def comment_reply_view(request, comment_id):
    parent = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.parent = parent
            reply.post = parent.post
            reply.author = request.user
            reply.save()
            return redirect('post_detail', post_id=parent.post.id)
    else:
        form = CommentForm()
    return render(request, 'siqposts/reply_comment.html', {'form': form, 'parent': parent})


def comment_like_view(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    user = request.user
    if user in comment.likes.all():
        comment.likes.remove(user)
    else:
        comment.likes.add(user)
    return JsonResponse({'likes': comment.likes.count()})


def comment_edit_view(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=comment.post.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'siqposts/edit_comment.html', {'form': form, 'comment': comment})


def comment_delete_view(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    post_id = comment.post.id
    if request.method == 'POST':
        comment.delete()
        return redirect('post_detail', post_id=post_id)
    return render(request, 'siqposts/delete_comment.html', {'comment': comment})


def image_upload_view(request):
    return HttpResponse("Image upload endpoint")


def video_upload_view(request):
    return HttpResponse("Video upload endpoint")


def audio_upload_view(request):
    return HttpResponse("Audio upload endpoint")


def poll_create_view(request):
    return HttpResponse("Poll creation endpoint")


def poll_vote_view(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    option_id = request.POST.get('option_id')
    option = get_object_or_404(PollOption, id=option_id, poll=poll)
    option.votes.add(request.user)
    return JsonResponse({'vote_count': option.vote_count()})


def post_search_view(request):
    query = request.GET.get('q', '')
    results = CivicPost.objects.filter(title__icontains=query)
    return render(request, 'siqposts/search_results.html', {'results': results, 'query': query})


def tagged_posts_view(request, tag):
    posts = CivicPost.objects.filter(tags__icontains=tag)
    return render(request, 'siqposts/tagged_posts.html', {'posts': posts, 'tag': tag})


def post_flag_view(request, post_id):
    post = get_object_or_404(CivicPost, id=post_id)
    post.is_flagged = True
    post.save()
    return JsonResponse({'flagged': True})


def comment_flag_view(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.is_flagged = True
    comment.save()
    return JsonResponse({'flagged': True})


def smart_feed_view(request):
    posts = CivicPost.objects.filter(visibility='public').order_by('-views')[:20]
    return render(request, 'siqposts/smart_feed.html', {'posts': posts})


def trending_feed_view(request):
    posts = CivicPost.objects.filter(visibility='public').order_by('-likes')[:20]
    return render(request, 'siqposts/trending_feed.html', {'posts': posts})
