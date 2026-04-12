# Quick Fix for Windows Setup

## The Issue
You encountered a MySQL driver issue on Windows. I've fixed it by switching to SQLite for development.

## What Changed
1. ✅ Settings updated to use SQLite (no MySQL needed for development)
2. ✅ Requirements updated (removed problematic mysqlclient)
3. ✅ Created Windows-specific setup guide

## Next Steps

### Step 1: Close any running Django processes
Press `Ctrl+C` in any terminal running Django

### Step 2: Delete the database file
```bash
del db.sqlite3
```

If you get "file in use" error, close all terminals and try again.

### Step 3: Run migrations
```bash
python manage.py migrate
```

### Step 4: Load categories
```bash
python manage.py loaddata categories
```

### Step 5: Create admin user
```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin account.

### Step 6: Run the server
```bash
python manage.py runserver
```

### Step 7: Access the application
- **Homepage**: http://localhost:8000
- **Admin Panel**: http://localhost:8000/admin
- **API**: http://localhost:8000/api/

---

## Alternative: Use the Reset Script

I've created a batch file that does all this automatically:

```bash
reset_db.bat
```

This will:
1. Delete the database
2. Run migrations
3. Load categories
4. Prompt you for next steps

---

## What's Different from PHP?

### Database
- **PHP**: MySQL required
- **Django (Dev)**: SQLite (no setup needed)
- **Django (Prod)**: MySQL/PostgreSQL

### Why SQLite for Development?
- ✅ No installation required
- ✅ No driver issues on Windows
- ✅ Perfect for learning and testing
- ✅ Easy to reset (just delete the file)
- ✅ Can switch to MySQL later

### When to Use MySQL?
- Production deployment
- Team collaboration (shared database)
- Advanced features needed

---

## Troubleshooting

### "Migration is applied before its dependency"
```bash
# Delete database and start fresh
del db.sqlite3
python manage.py migrate
```

### "File is being used by another process"
1. Close all terminals
2. Close VS Code or your IDE
3. Try again

### "No module named 'marketplace'"
Make sure you're in the correct directory:
```bash
cd ashesi_market_django
```

### "python is not recognized"
Use full path:
```bash
py manage.py runserver
```

---

## Full Clean Setup

If you want to start completely fresh:

```bash
# 1. Delete database
del db.sqlite3

# 2. Delete migrations (optional)
rmdir /s marketplace\migrations
mkdir marketplace\migrations
echo # Migrations > marketplace\migrations\__init__.py

# 3. Create migrations
python manage.py makemigrations marketplace

# 4. Apply migrations
python manage.py migrate

# 5. Load data
python manage.py loaddata categories

# 6. Create admin
python manage.py createsuperuser

# 7. Run server
python manage.py runserver
```

---

## Success Checklist

- [ ] Database file deleted (if existed)
- [ ] Migrations run successfully
- [ ] Categories loaded
- [ ] Admin user created
- [ ] Server starts without errors
- [ ] Can access http://localhost:8000
- [ ] Can login to admin panel

---

## Next Steps After Setup

1. **Explore the Admin Panel**
   - Go to http://localhost:8000/admin
   - Login with your superuser credentials
   - Add some test products

2. **Test the API**
   - Go to http://localhost:8000/api/
   - Try the endpoints
   - Use Postman for testing

3. **Read the Documentation**
   - README.md - Overview
   - WINDOWS_SETUP.md - Windows-specific guide
   - QUICKSTART.md - Detailed setup
   - MIGRATION_GUIDE.md - PHP to Django

4. **Start Development**
   - Create products
   - Test the cart
   - Try the checkout flow

---

## Need Help?

- **Windows Setup**: See WINDOWS_SETUP.md
- **General Setup**: See QUICKSTART.md
- **PHP Conversion**: See MIGRATION_GUIDE.md
- **Deployment**: See DEPLOYMENT.md

---

## Summary

✅ **Problem**: MySQL driver won't install on Windows  
✅ **Solution**: Using SQLite for development  
✅ **Result**: No database setup needed, works immediately  
✅ **Future**: Can switch to MySQL for production  

**You're all set! Just follow the steps above and you'll be running in minutes.**
