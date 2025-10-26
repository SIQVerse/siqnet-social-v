import os
import sys
import django
from channels.routing import get_default_application

# ✅ Set default settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "siqnet_backend.settings")

# ✅ Add project root to sys.path for modular imports
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(PROJECT_ROOT, '..'))

# ✅ Set environment flags for production (can be overridden externally)
os.environ.setdefault("SIQNET_ENV", "production")

# ✅ Initialize Django
django.setup()

# ✅ Load ASGI application (includes WebSocket routing)
application = get_default_application()
