from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render

# 🏠 Homepage view
def home_view(request):
    return render(request, 'home.html')

# 🔐 JWT Authentication
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# 📘 Swagger Documentation
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="SIQNet API",
        default_version='v1',
        description="Civic engagement platform API",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

# 🚦 URL Patterns
urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('auth/', include('apps.userauth.urls')),
    path('siqposts/', include('apps.siqposts.urls')),
    path('api/v1/', include('apps.api.urls')),
    path('api/v1/siqposts/', include('apps.siqposts.api_urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

# 📦 Static & Media Files (only in development)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
