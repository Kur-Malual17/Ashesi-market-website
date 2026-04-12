@echo off
echo ========================================
echo   Restarting Ashesi Market Django Server
echo ========================================
echo.
echo IMPORTANT: This will restart the server with updated settings
echo Press Ctrl+C to stop the server when needed
echo.
echo Server will be available at: http://localhost:8000
echo Admin panel: http://localhost:8000/admin/
echo API docs: http://localhost:8000/api/
echo.
echo ========================================
echo.
python manage.py runserver
