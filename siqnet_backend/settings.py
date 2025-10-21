import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Security
DEBUG = False  # Set to True only in development
ALLOWED_HOSTS = ["your-backend-domain.com", "localhost", "127.0.0.1"]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third-party
    'corsheaders',
    # Your apps
    'userauth',
    'community',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Must be first for CORS
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CORS setup
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # React dev server
    "https://your-frontend-domain.com",  # Production frontend
]

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
