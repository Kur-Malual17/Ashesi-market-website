# Windows Setup Guide

Special instructions for setting up Ashesi Market Django on Windows.

## Quick Start (SQLite - Recommended for Development)

The project is now configured to use SQLite by default on Windows, which requires no additional database setup.

```bash
# 1. Create virtual environment
python -m venv venv
venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run migrations
python manage.py migrate

# 4. Load initial data
python manage.py loaddata categories

# 5. Create admin user
python manage.py createsuperuser

# 6. Run server
python manage.py runserver
```

Visit: http://localhost:8000

---

## Using MySQL on Windows (Optional)

If you want to use MySQL instead of SQLite, follow these steps:

### Option 1: Use PyMySQL (Easier)

1. Install PyMySQL:
```bash
pip install pymysql
```

2. Add to `ashesi_market/__init__.py`:
```python
import pymysql
pymysql.install_as_MySQLdb()
```

3. Update `settings.py` to use MySQL configuration (uncomment the MySQL DATABASES section)

### Option 2: Install mysqlclient Pre-compiled Wheel

1. Download the appropriate wheel from:
   https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient

   For Python 3.8 64-bit:
   `mysqlclient‑2.2.0‑cp38‑cp38‑win_amd64.whl`

2. Install the wheel:
```bash
pip install path\to\mysqlclient‑2.2.0‑cp38‑cp38‑win_amd64.whl
```

3. Update `settings.py` to use MySQL configuration

### Option 3: Install MySQL Connector/C

1. Download and install MySQL Connector/C:
   https://dev.mysql.com/downloads/connector/c/

2. Add to system PATH:
   - `C:\Program Files\MySQL\MySQL Connector C 8.0\lib`
   - `C:\Program Files\MySQL\MySQL Connector C 8.0\include`

3. Install mysqlclient:
```bash
pip install mysqlclient
```

---

## Common Windows Issues

### Issue 1: pip is not recognized
```bash
python -m pip install -r requirements.txt
```

### Issue 2: Virtual environment activation fails
```bash
# Use PowerShell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
venv\Scripts\Activate.ps1

# Or use Command Prompt
venv\Scripts\activate.bat
```

### Issue 3: Port 8000 already in use
```bash
python manage.py runserver 8001
```

### Issue 4: Permission denied on media folder
Run Command Prompt or PowerShell as Administrator

---

## SQLite vs MySQL

### SQLite (Default)
**Pros:**
- No installation required
- Works immediately
- Perfect for development
- Easy to reset (just delete db.sqlite3)

**Cons:**
- Not suitable for production
- Limited concurrent writes
- No user management

### MySQL
**Pros:**
- Production-ready
- Better performance
- Concurrent access
- Advanced features

**Cons:**
- Requires installation
- More complex setup on Windows
- Driver installation issues

---

## Switching from SQLite to MySQL

1. Export data from SQLite:
```bash
python manage.py dumpdata > data.json
```

2. Update `settings.py` to use MySQL

3. Create MySQL database:
```sql
CREATE DATABASE ashesi_market CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Import data:
```bash
python manage.py loaddata data.json
```

---

## Development Workflow

### Daily Development
```bash
# Activate virtual environment
venv\Scripts\activate

# Run server
python manage.py runserver

# In another terminal (for migrations)
python manage.py makemigrations
python manage.py migrate
```

### Reset Database (SQLite)
```bash
# Delete database
del db.sqlite3

# Recreate
python manage.py migrate
python manage.py loaddata categories
python manage.py createsuperuser
```

---

## Production Deployment

For production, you should:
1. Use MySQL or PostgreSQL (not SQLite)
2. Set `DEBUG=False`
3. Use a proper web server (Gunicorn + Nginx)
4. See DEPLOYMENT.md for details

---

## Troubleshooting

### Django not found
```bash
pip install django
```

### Module not found errors
```bash
pip install -r requirements.txt
```

### Database locked (SQLite)
- Close all connections
- Restart the server
- Check for other processes using the database

### Static files not loading
```bash
python manage.py collectstatic
```

---

## Recommended Tools for Windows

- **Python**: Python 3.8+ from python.org
- **IDE**: VS Code with Python extension
- **Database**: SQLite Browser (for viewing SQLite databases)
- **API Testing**: Postman or Thunder Client (VS Code extension)
- **Terminal**: Windows Terminal or PowerShell

---

## Next Steps

1. ✅ Setup complete with SQLite
2. Explore the admin panel: http://localhost:8000/admin
3. Test the API: http://localhost:8000/api/
4. Read the documentation: README.md
5. When ready for production, switch to MySQL

---

## Support

- Main README: README.md
- Quick Start: QUICKSTART.md
- Deployment: DEPLOYMENT.md
- Django Docs: https://docs.djangoproject.com/
