import os

# 🌍 Determine environment
env = os.environ.get('DJANGO_ENV', 'dev').lower()

# 🔁 Load appropriate settings module
if env == 'prod':
    from .production import *
elif env == 'dev':
    from .development import *
else:
    raise ValueError(f"Unknown DJANGO_ENV: {env}")
