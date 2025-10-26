@echo off
cd /d "C:\Users\Uncle Sam\siqnet-social-v"
call venv\Scripts\activate
python manage.py runserver 0.0.0.0:8000
pause
