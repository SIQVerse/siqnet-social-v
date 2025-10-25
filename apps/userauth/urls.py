from django.urls import path
from . import views

urlpatterns = [
    # 🔐 Authentication
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # 👤 Profile & Identity
    path('profile/', views.profile_view, name='profile'),  # Current user's profile
    path('profile/edit/', views.profile_edit_view, name='profile_edit'),
    path('profile/<str:username>/', views.public_profile_view, name='public_profile'),  # Public profile by username

    # ⚙️ Account Settings
    path('settings/', views.account_settings_view, name='account_settings'),
    path('settings/security/', views.security_settings_view, name='security_settings'),

    # 🏅 Verification & Badges
    path('verify/', views.verification_request_view, name='verification_request'),
    path('badges/', views.user_badges_view, name='user_badges'),

    # 📊 Activity & Analytics
    path('activity/', views.user_activity_view, name='user_activity'),
]
