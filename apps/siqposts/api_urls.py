from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CivicPostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', CivicPostViewSet, basename='civicpost')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
]
