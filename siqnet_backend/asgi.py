import os
import django
from channels.routing import get_default_application

# Set the default settings module for Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "siqnet_backend.settings")

# Setup Django
django.setup()

# Get the default ASGI application (includes WebSocket routing)
application = get_default_application()
