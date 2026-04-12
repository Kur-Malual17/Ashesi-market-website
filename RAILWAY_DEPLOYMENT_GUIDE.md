# Railway + Vercel Deployment Guide

## What I Fixed

1. **Added gunicorn** to `requirements.txt` - Railway needs this to run your Django app
2. **Created Procfile** - Tells Railway how to start your app
3. **Created railway.toml** - Railway configuration with auto-migration
4. **Updated Django settings** - Added support for Railway and Vercel domains
5. **Updated CORS settings** - Your Vercel frontend can now communicate with Railway backend

## Railway Backend Deployment Steps

### 1. Push Your Changes to Git

```bash
cd ashesi_market_django
git add .
git commit -m "Add Railway deployment configuration"
git push
```

### 2. Configure Environment Variables on Railway

Go to your Railway project settings and add these environment variables:

```
DEBUG=False
SECRET_KEY=your-super-secret-key-here-generate-a-new-one
ALLOWED_HOSTS=.railway.app,.vercel.app
CORS_ALLOWED_ORIGINS=https://ashesi-market-website.vercel.app
CSRF_TRUSTED_ORIGINS=https://ashesi-market-website.vercel.app
SESSION_COOKIE_SAMESITE=None
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SAMESITE=None
CSRF_COOKIE_SECURE=True
```

**Important:** Generate a new SECRET_KEY for production. You can use this Python command:
```python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 3. Railway Should Auto-Deploy

After pushing your changes, Railway should automatically:
- Install dependencies (including gunicorn)
- Run migrations
- Start the server with gunicorn

### 4. Get Your Railway Backend URL

Once deployed, Railway will give you a URL like:
`https://your-app-name.railway.app`

## Vercel Frontend Configuration

### Update Your Frontend API URL

You need to update the frontend to use your Railway backend URL instead of localhost.

**Option 1: Environment Variable (Recommended)**

1. Go to your Vercel project settings
2. Add environment variable:
   - Name: `VITE_API_BASE_URL` or `NEXT_PUBLIC_API_BASE_URL`
   - Value: `https://your-railway-app.railway.app/api`

3. Update `ashesi_market_frontend/js/config.js`:

```javascript
// API Configuration
const API_BASE_URL = window.ENV?.API_BASE_URL || 'https://your-railway-app.railway.app/api';
```

**Option 2: Direct Update (Quick Fix)**

Update `ashesi_market_frontend/js/config.js`:

```javascript
// API Configuration
const API_BASE_URL = 'https://your-railway-app.railway.app/api';
```

Then redeploy to Vercel:
```bash
cd ashesi_market_frontend
git add .
git commit -m "Update API URL to Railway backend"
git push
```

## Testing Your Deployment

1. Visit your Vercel frontend: `https://ashesi-market-website.vercel.app`
2. Try to register/login
3. Check browser console for any CORS errors
4. Test creating a product, adding to cart, etc.

## Troubleshooting

### CORS Errors
If you see CORS errors, make sure:
- Your Railway backend has the Vercel URL in `CORS_ALLOWED_ORIGINS`
- Your Railway backend has the Vercel URL in `CSRF_TRUSTED_ORIGINS`
- Environment variables are set correctly on Railway

### Session/Cookie Issues
For cross-domain cookies to work:
- `SESSION_COOKIE_SAMESITE=None`
- `SESSION_COOKIE_SECURE=True`
- `CSRF_COOKIE_SAMESITE=None`
- `CSRF_COOKIE_SECURE=True`

These are already configured in the updated settings.py

### Static Files Not Loading
Railway should serve static files automatically with the configuration I added.

### Database Issues
Railway uses SQLite by default. For production, consider:
- Railway's PostgreSQL addon (recommended)
- External database service

To use PostgreSQL, add to Railway environment variables:
```
DATABASE_URL=postgresql://user:password@host:port/dbname
```

And update your Django settings to use `dj-database-url` package.

## Next Steps

1. Push the changes to git
2. Set environment variables on Railway
3. Wait for Railway to redeploy
4. Update frontend config with Railway URL
5. Test everything!

Your backend should now start successfully on Railway! 🚀
