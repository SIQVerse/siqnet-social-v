import os
import django
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
import apps.messaging.routing

# 🌍 Set Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "siqnet_backend.settings")

# 🧠 Initialize Django
django.setup()

# 🚦 ASGI application with HTTP and WebSocket support
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            apps.messaging.routing.websocket_urlpatterns
        )
    ),
})
