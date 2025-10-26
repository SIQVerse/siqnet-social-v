from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import CivicPost, Comment, Poll
from .forms import CivicPostForm, CommentForm
from .serializers import CivicPostSerializer, CommentSerializer

# 🌐 DRF ViewSets
class CivicPostViewSet(viewsets.ModelViewSet):
    queryset = CivicPost.objects.all().order_by('-created_at')
    serializer_class = CivicPostSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        post = self.get_object()
        user = request.user
        if user in post.likes.all():
            post.likes.remove(user)
        else:
            post.likes.add(user)
        return Response({'likes': post.likes.count()})

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

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        comment = self.get_object()
        user = request.user
        if user in comment.likes.all():
            comment.likes.remove(user)
        else:
            comment.likes.add(user)
        return Response({'likes': comment.likes.count()})

# 📝 Django views (unchanged)
# [Your original Django views remain intact below this section]
# You can keep all the post_list_view, post_detail_view, etc. as-is
