@echo off
echo Starting Ashesi Market Frontend Server...
echo.
echo Frontend will be available at: http://localhost:8080
echo Press Ctrl+C to stop the server
echo.
python -m http.server 8080
