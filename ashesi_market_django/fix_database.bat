@echo off
echo ========================================
echo  Fixing Database - Ashesi Market
echo ========================================
echo.

echo Step 1: Stopping any Django processes...
taskkill /F /IM python.exe 2>nul
timeout /t 2 /nobreak >nul

echo Step 2: Deleting old database...
if exist db.sqlite3 (
    del /F /Q db.sqlite3
    echo Database deleted!
) else (
    echo No database file found.
)

echo Step 3: Deleting migration files...
if exist marketplace\migrations\0001_initial.py (
    del /F /Q marketplace\migrations\0001_initial.py
    echo Migration files deleted!
)

echo Step 4: Creating fresh migrations...
python manage.py makemigrations marketplace

echo Step 5: Running migrations...
python manage.py migrate

echo Step 6: Loading categories...
python manage.py loaddata categories

echo.
echo ========================================
echo  Database Fixed!
echo ========================================
echo.
echo Next steps:
echo 1. Create superuser: python manage.py createsuperuser
echo 2. Run server: python manage.py runserver
echo.
pause
