import os
from django.apps import AppConfig

class SiqPostsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.siqposts'

    # Optional: explicitly set the app path if needed
    path = os.path.abspath(os.path.dirname(__file__))
