from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# 🔐 JWT & Swagger
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# 📘 Swagger schema configuration
schema_view = get_schema_view(
    openapi.Info(
        title="SIQNet API",
        default_version='v1',
        description="Civic engagement platform API",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # 🛠 Admin Panel
    path('admin/', admin.site.urls),

    # 🔐 Authentication & Profiles
    path('auth/', include('apps.userauth.urls')),

    # 📝 Posts, Comments, Engagement (Web views)
    path('siqposts/', include('apps.siqposts.urls')),

    # 👥 Groups & Communities
    # path('groups/', include('apps.groups.urls')),  # Uncomment when ready

    # 🔔 Notifications
    # path('notifications/', include('apps.notifications.urls')),  # Uncomment when ready

    # 📦 Media Management
    # path('mediahub/', include('apps.mediahub.urls')),  # Uncomment when ready

    # 📊 Analytics & Insights
    # path('analytics/', include('apps.analytics.urls')),  # Uncomment when ready

    # 🌐 API Access (for mobile or frontend apps)
    path('api/v1/', include('apps.api.urls')),

    # 🌐 DRF API for siqposts (Post & Comment endpoints)
    path('api/v1/siqposts/', include('apps.siqposts.api_urls')),

    # ❤️ Health Check & Monitoring
    # path('health/', include('apps.healthcheck.urls')),  # Uncomment when ready

    # 🔐 JWT Authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # 📘 Swagger Docs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

# 📁 Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
