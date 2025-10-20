from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('apps.userauth.urls')),     # Routes for userauth app
    path('posts/', include('apps.siqposts.urls')),    # Routes for siqposts app
]
