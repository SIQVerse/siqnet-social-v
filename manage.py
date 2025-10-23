#!/usr/bin/env python
"""SIQNet's command-line utility for administrative tasks."""
import os
import sys
import logging

def main():
    """Run administrative tasks with enhanced environment awareness."""
    # Set default settings module, allowing override via environment variable
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        os.environ.get("DJANGO_SETTINGS_MODULE", "siqnet_backend.settings")
    )

    # Optional: Log environment info for debugging and deployment
    env = os.environ.get("SIQNET_ENV", "development")
    logging.basicConfig(level=logging.INFO)
    logging.info(f"Starting SIQNet manage.py in {env} mode.")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Make sure it's installed and "
            "available on your PYTHONPATH environment variable. Did you "
            "forget to activate your virtual environment?"
        ) from exc

    # Optional: Add profiling or debug hooks here
    # if '--profile' in sys.argv:
    #     import cProfile
    #     cProfile.run('execute_from_command_line(sys.argv)')

    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    main()
