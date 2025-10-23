from django.urls import path
from . import views

urlpatterns = [
    # 📝 Post Views
    path('', views.post_list_view, name='post_list'),
    path('<int:post_id>/', views.post_detail_view, name='post_detail'),
    path('create/', views.post_create_view, name='post_create'),
    path('<int:post_id>/edit/', views.post_edit_view, name='post_edit'),
    path('<int:post_id>/delete/', views.post_delete_view, name='post_delete'),

    # ❤️ Engagement
    path('<int:post_id>/like/', views.post_like_view, name='post_like'),
    path('<int:post_id>/share/', views.post_share_view, name='post_share'),
    path('<int:post_id>/view/', views.post_view_tracker, name='post_view'),

    # 💬 Comments
    path('<int:post_id>/comment/', views.comment_create_view, name='comment_create'),
    path('comment/<int:comment_id>/reply/', views.comment_reply_view, name='comment_reply'),
    path('comment/<int:comment_id>/like/', views.comment_like_view, name='comment_like'),
    path('comment/<int:comment_id>/edit/', views.comment_edit_view, name='comment_edit'),
    path('comment/<int:comment_id>/delete/', views.comment_delete_view, name='comment_delete'),

    # 🖼️ Media Uploads
    path('upload/image/', views.image_upload_view, name='image_upload'),
    path('upload/video/', views.video_upload_view, name='video_upload'),
    path('upload/audio/', views.audio_upload_view, name='audio_upload'),

    # 📊 Polls
    path('poll/create/', views.poll_create_view, name='poll_create'),
    path('poll/<int:poll_id>/vote/', views.poll_vote_view, name='poll_vote'),

    # 🔍 Search & Tags
    path('search/', views.post_search_view, name='post_search'),
    path('tag/<str:tag>/', views.tagged_posts_view, name='tagged_posts'),

    # 🛡️ Moderation
    path('<int:post_id>/flag/', views.post_flag_view, name='post_flag'),
    path('comment/<int:comment_id>/flag/', views.comment_flag_view, name='comment_flag'),

    # 🧠 Smart Feed
    path('feed/smart/', views.smart_feed_view, name='smart_feed'),
    path('feed/trending/', views.trending_feed_view, name='trending_feed'),
]
