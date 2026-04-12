# Database Setup Guide - Railway PostgreSQL

## Current Problem

You're using **SQLite** (a file-based database) on Railway, which has a major issue:

❌ **Railway's filesystem is ephemeral**
- Every deployment deletes the database file
- All users, products, orders are lost
- You start fresh each time

This is why:
- Users can register but disappear after redeployment
- Login fails after Railway redeploys
- Data doesn't persist

## Solution: PostgreSQL on Railway

Railway provides **free PostgreSQL databases** that persist data permanently.

## Setup Steps

### Step 1: Add PostgreSQL to Railway

1. Go to your Railway project dashboard
2. Click **"+ New"** button
3. Select **"Database"**
4. Choose **"PostgreSQL"**
5. Railway will create a PostgreSQL database

### Step 2: Link Database to Django Service

Railway automatically creates a `DATABASE_URL` environment variable when you add PostgreSQL to your project.

**Verify it's linked:**
1. Go to your Django service in Railway
2. Click on "Variables" tab
3. You should see `DATABASE_URL` (automatically added)
4. It looks like: `postgresql://user:password@host:port/dbname`

**If you don't see DATABASE_URL:**
1. Go to PostgreSQL service
2. Click "Connect"
3. Copy the "DATABASE_URL"
4. Go to Django service → Variables
5. Add: `DATABASE_URL=<paste-the-url>`

### Step 3: Deploy Backend Changes

```bash
cd ashesi_market_django
git add .
git commit -m "Add PostgreSQL database support"
git push
```

Railway will:
1. Install `psycopg2-binary` (PostgreSQL driver)
2. Install `dj-database-url` (database URL parser)
3. Connect to PostgreSQL instead of SQLite
4. Run migrations on PostgreSQL
5. Create superuser (if environment variables are set)

### Step 4: Verify Database Connection

Check Railway logs after deployment:

**Success looks like:**
```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, marketplace, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  ...
Superuser created successfully: your-email@example.com
```

**If you see errors:**
- Check that `DATABASE_URL` exists in environment variables
- Check Railway logs for connection errors

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                         YOUR SETUP                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────┐         ┌──────────────┐                │
│  │   Vercel     │         │   Railway    │                │
│  │  (Frontend)  │────────▶│  (Backend)   │                │
│  │              │  HTTPS  │   Django     │                │
│  │  HTML/CSS/JS │         │   + API      │                │
│  └──────────────┘         └──────┬───────┘                │
│                                   │                         │
│                                   │ DATABASE_URL            │
│                                   │                         │
│                           ┌───────▼────────┐               │
│                           │   PostgreSQL   │               │
│                           │   (Railway)    │               │
│                           │                │               │
│                           │  Persistent    │               │
│                           │  Storage       │               │
│                           └────────────────┘               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Database Locations

### Before (SQLite):
- **Location:** `/app/db.sqlite3` on Railway container
- **Persistence:** ❌ Deleted on every deployment
- **Backup:** ❌ No automatic backups
- **Scalability:** ❌ Can't scale to multiple servers

### After (PostgreSQL):
- **Location:** Separate PostgreSQL service on Railway
- **Persistence:** ✅ Data persists across deployments
- **Backup:** ✅ Railway handles backups
- **Scalability:** ✅ Can scale independently

## What Happens to Existing Data?

⚠️ **Important:** When you switch to PostgreSQL, you start with a **fresh database**.

Any data in SQLite (which gets deleted anyway) will not be transferred.

**This is fine because:**
- SQLite data was being deleted on each deployment anyway
- You probably don't have important data yet
- Fresh start with persistent database is better

## After PostgreSQL Setup

### Create Superuser Again

Since it's a fresh database, create superuser:

**Option 1: Automatic (if environment variables are set)**
Railway will auto-create on deployment if you have:
```
DJANGO_SUPERUSER_EMAIL=your-email@example.com
DJANGO_SUPERUSER_PASSWORD=YourPassword123
```

**Option 2: Manual (using Railway CLI)**
```bash
railway login
cd ashesi_market_django
railway link
railway run python manage.py createsuperuser
```

### Test Everything

1. **Register a new user**
   - Should work and persist

2. **Login**
   - Should work with registered user

3. **Redeploy Railway**
   - Go to Railway → Redeploy
   - After redeployment, login again
   - ✅ Should still work! (data persisted)

4. **Create products, orders**
   - All data will persist across deployments

## Environment Variables Summary

Your Railway Django service should have:

```
# Required
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=.railway.app,.vercel.app

# Database (automatically added by Railway)
DATABASE_URL=postgresql://user:password@host:port/dbname

# CORS
CORS_ALLOWED_ORIGINS=https://ashesi-market-website.vercel.app
CSRF_TRUSTED_ORIGINS=https://ashesi-market-website.vercel.app

# Optional: Auto-create superuser
DJANGO_SUPERUSER_EMAIL=your-email@example.com
DJANGO_SUPERUSER_PASSWORD=YourPassword123
DJANGO_SUPERUSER_FIRST_NAME=Admin
DJANGO_SUPERUSER_LAST_NAME=User
```

## Checking Your Database

### View Database in Railway:
1. Go to Railway dashboard
2. Click PostgreSQL service
3. Click "Data" tab
4. You can see tables and data

### Connect with Database Client:
1. Get connection details from Railway PostgreSQL service
2. Use tools like:
   - pgAdmin
   - DBeaver
   - TablePlus
   - psql command line

## Cost

- **PostgreSQL on Railway:** FREE (up to 500MB)
- **Django on Railway:** FREE (up to 500 hours/month)
- **Vercel Frontend:** FREE

All within free tiers! 🎉

## Troubleshooting

### "Could not connect to database"
- Check `DATABASE_URL` exists in environment variables
- Check PostgreSQL service is running
- Check Railway logs for connection errors

### "relation does not exist"
- Migrations didn't run
- Check Railway logs
- Manually run: `railway run python manage.py migrate`

### "password authentication failed"
- `DATABASE_URL` is incorrect
- Regenerate from PostgreSQL service

### Data still disappearing
- Verify you're using PostgreSQL, not SQLite
- Check Railway logs for "Using database: postgresql"
- Check `DATABASE_URL` is set

## Summary

**Before:**
- SQLite file on Railway
- Data deleted on every deployment
- No persistence

**After:**
- PostgreSQL database on Railway
- Data persists forever
- Automatic backups
- Production-ready

Deploy the changes and add PostgreSQL to Railway - your data will finally persist! 🚀
