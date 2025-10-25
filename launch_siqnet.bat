@echo off
REM Activate virtual environment
call venv\Scripts\activate

REM Navigate to project directory
cd /d "C:\Users\Uncle Sam\siqnet-social-v"

REM Run Django setup
python manage.py migrate
python manage.py collectstatic --noinput

REM Start server with Waitress (Gunicorn doesn't work on Windows)
waitress-serve --port=8000 siqnet_backend.wsgi:application
