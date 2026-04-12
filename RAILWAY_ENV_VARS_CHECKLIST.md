# Railway Environment Variables Checklist

## Required Environment Variables

Go to Railway → Your Django Service → Variables

Make sure you have ALL of these:

### 1. Database
```
DATABASE_URL=postgresql://postgres:rbPzVpKUvmepOKVlIIGZrvDcBbfRzkDN@postgres-h30n.railway.internal:5432/YOUR_NEW_DATABASE_NAME
```
(Use your new PostgreSQL database URL)

### 2. Django Settings
```
SECRET_KEY=your-super-secret-key-here
DEBUG=False
```

### 3. CORS & CSRF (CRITICAL for Vercel to work!)
```
ALLOWED_HOSTS=.railway.app,.vercel.app,ashesi-market-website.vercel.app,ashesi-market-website-production.up.railway.app

CORS_ALLOWED_ORIGINS=https://ashesi-market-website.vercel.app,https://ashesi-market-website-git-main-kur-malual17s-projects.vercel.app

CSRF_TRUSTED_ORIGINS=https://ashesi-market-website.vercel.app,https://ashesi-market-website-git-main-kur-malual17s-projects.vercel.app,https://ashesi-market-website-production.up.railway.app
```

### 4. Optional: Auto-create Superuser
```
DJANGO_SUPERUSER_EMAIL=your-email@ashesi.edu.gh
DJANGO_SUPERUSER_PASSWORD=YourSecurePassword123
DJANGO_SUPERUSER_FIRST_NAME=Admin
DJANGO_SUPERUSER_LAST_NAME=User
```

## Variables to DELETE (if they exist)

These cause conflicts:
- ❌ `SESSION_COOKIE_SAMESITE`
- ❌ `SESSION_COOKIE_SECURE`
- ❌ `CSRF_COOKIE_SAMESITE`
- ❌ `CSRF_COOKIE_SECURE`

## After Setting Variables

1. Railway will auto-redeploy
2. Check logs for successful startup
3. Test Vercel frontend

## Quick Test

After setting variables, test in browser console:

```javascript
fetch('https://ashesi-market-website-production.up.railway.app/api/categories/')
  .then(r => r.json())
  .then(d => console.log('Success:', d))
  .catch(e => console.error('Error:', e));
```

Should see: `Success: []`

If you see CORS error, the CORS_ALLOWED_ORIGINS is not set correctly!
