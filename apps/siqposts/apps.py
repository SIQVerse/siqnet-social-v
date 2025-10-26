from django.apps import AppConfig

class SiqPostsConfig(AppConfig):
    """
    Configuration for the siqposts app, including automatic signal registration.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.siqposts'

    def ready(self):
        # Import signals to ensure they are registered when the app is loaded
        import apps.siqposts.signals
