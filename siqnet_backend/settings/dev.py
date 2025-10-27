from .base import *

# 🐛 Enable debug mode for development
DEBUG = True

# 🌐 Allow all hosts during development
ALLOWED_HOSTS = ['*']

# ✉️ Console email backend for testing
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
