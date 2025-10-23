import os
import sys
from django.core.wsgi import get_wsgi_application

# ✅ Set default settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "siqnet_backend.settings")

# ✅ Add project root to sys.path for modular imports
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(PROJECT_ROOT, '..'))

# ✅ Optional: Set environment flags for production
os.environ.setdefault("SIQNET_ENV", "production")

# ✅ Optional: Configure logging (can be expanded in settings.py)
if os.environ.get("SIQNET_ENV") == "production":
    import logging
    logging.basicConfig(level=logging.INFO)
    logging.info("WSGI application starting in production mode.")

# ✅ Optional: Security headers (if using WSGI middleware)
# from django.middleware.security import SecurityMiddleware
# application = SecurityMiddleware(get_wsgi_application())

# ✅ Final WSGI application
application = get_wsgi_application()
