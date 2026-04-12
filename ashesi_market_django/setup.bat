@echo off
REM Ashesi Market Django Setup Script for Windows

echo === Ashesi Market Django Setup ===
echo.

REM Check Python version
python --version

REM Create virtual environment
echo Creating virtual environment...
python -m venv venv

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo Installing dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt

REM Copy environment file
if not exist .env (
    echo Creating .env file...
    copy .env.example .env
    echo Please edit .env with your database credentials
)

REM Create media directories
echo Creating media directories...
if not exist media\products mkdir media\products
if not exist media\id_images mkdir media\id_images

REM Run migrations
echo Running migrations...
python manage.py makemigrations
python manage.py migrate

REM Load initial data
echo Loading categories...
python manage.py loaddata categories

REM Create superuser
echo.
echo Create a superuser account for admin access:
python manage.py createsuperuser

echo.
echo === Setup Complete! ===
echo.
echo To start the development server:
echo   venv\Scripts\activate
echo   python manage.py runserver
echo.
echo Then visit: http://localhost:8000
echo Admin panel: http://localhost:8000/admin

pause
