@echo off
echo Resetting database...
echo.
echo Please close any programs that might be using the database.
echo Press any key to continue or Ctrl+C to cancel...
pause > nul

echo.
echo Deleting database file...
if exist db.sqlite3 (
    del /F db.sqlite3
    echo Database deleted.
) else (
    echo No database file found.
)

echo.
echo Running migrations...
python manage.py migrate

echo.
echo Loading initial data...
python manage.py loaddata categories

echo.
echo Database reset complete!
echo.
echo Next steps:
echo 1. Create a superuser: python manage.py createsuperuser
echo 2. Run the server: python manage.py runserver
echo.
pause
