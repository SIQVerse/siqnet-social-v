from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list_view, name='post_list'),
    path('<int:post_id>/', views.post_detail_view, name='post_detail'),
    path('create/', views.post_create_view, name='post_create'),
    path('<int:post_id>/edit/', views.post_edit_view, name='post_edit'),
    path('<int:post_id>/delete/', views.post_delete_view, name='post_delete'),
]
