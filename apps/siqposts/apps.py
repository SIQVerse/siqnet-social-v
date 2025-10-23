import os
from django.apps import AppConfig

class SiqPostsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.siqposts'
    path = os.path.abspath(os.path.dirname(__file__))
