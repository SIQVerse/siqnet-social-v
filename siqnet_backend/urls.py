from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 🛠 Admin Panel
    path('admin/', admin.site.urls),

    # 🔐 Authentication & Profiles
    path('auth/', include('apps.userauth.urls')),

    # 📝 Posts, Comments, Engagement
    path('siqposts/', include('apps.siqposts.urls')),

    # 💬 Messaging & Chat
    path('messages/', include('apps.messaging.urls')),

    # 👥 Groups & Communities
    path('groups/', include('apps.groups.urls')),

    # 🔔 Notifications
    path('notifications/', include('apps.notifications.urls')),

    # 📦 Media Management
    path('mediahub/', include('apps.mediahub.urls')),

    # 📊 Analytics & Insights
    path('analytics/', include('apps.analytics.urls')),

    # 🌐 API Access (for mobile or frontend apps)
    path('api/v1/', include('apps.api.urls')),

    # ❤️ Health Check & Monitoring
    path('health/', include('apps.healthcheck.urls')),
]

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
