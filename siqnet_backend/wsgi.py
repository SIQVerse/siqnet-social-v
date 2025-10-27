import os
import sys
import logging
from django.core.wsgi import get_wsgi_application

# 🌍 Set Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "siqnet_backend.settings")

# 📁 Ensure project root is in sys.path
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(PROJECT_ROOT, '..'))

# 🛡️ Set environment flag
os.environ.setdefault("SIQNET_ENV", "production")

# 📝 Configure logging for production
if os.environ.get("SIQNET_ENV") == "production":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[logging.StreamHandler()]
    )
    logging.info("WSGI application starting in production mode.")

# 🚀 Launch WSGI application
application = get_wsgi_application()
