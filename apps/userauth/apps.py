import os
from django.apps import AppConfig

class UserAuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.userauth'
    path = os.path.abspath(os.path.dirname(__file__))
