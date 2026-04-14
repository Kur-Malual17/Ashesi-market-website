# Cloudinary Image Storage Setup

## Why Cloudinary?

Railway's filesystem is ephemeral - uploaded images are deleted on every deployment. Cloudinary provides:
- ✅ Permanent image storage
- ✅ Automatic image optimization
- ✅ CDN delivery (fast worldwide)
- ✅ Image transformations (resize, crop, etc.)
- ✅ Free tier: 25GB storage, 25GB bandwidth/month

## Step 1: Get Cloudinary Credentials

1. Go to: https://cloudinary.com/console
2. Login to your account
3. On the dashboard, find "Account Details" or "API Keys" section
4. Copy these 3 values:
   - **Cloud Name** (e.g., `dxyz123abc`)
   - **API Key** (e.g., `123456789012345`)
   - **API Secret** (e.g., `abcdefghijklmnopqrstuvwxyz-ABC`)

## Step 2: Add to Railway Environment Variables

Go to Railway → Your Django Service → Variables → Add these:

```
CLOUDINARY_CLOUD_NAME=your-cloud-name
CLOUDINARY_API_KEY=your-api-key
CLOUDINARY_API_SECRET=your-api-secret
```

**Example:**
```
CLOUDINARY_CLOUD_NAME=dxyz123abc
CLOUDINARY_API_KEY=123456789012345
CLOUDINARY_API_SECRET=abcdefghijklmnopqrstuvwxyz-ABC
```

## Step 3: Deploy Backend

```bash
cd ashesi_market_django
git add .
git commit -m "Add Cloudinary image storage"
git push
```

Railway will:
1. Install Cloudinary packages
2. Configure Django to use Cloudinary
3. Redeploy

## Step 4: Test Image Upload

1. Go to your Vercel site
2. Login
3. Click "+ Sell"
4. Fill in product details
5. Upload an image
6. Submit

The image will be uploaded to Cloudinary!

## Step 5: Verify on Cloudinary

1. Go to Cloudinary dashboard
2. Click "Media Library"
3. You should see your uploaded images!

## How It Works

### Before (Railway Filesystem):
```
User uploads image → Saved to /app/media/ on Railway
                  → Deleted on next deployment ❌
```

### After (Cloudinary):
```
User uploads image → Uploaded to Cloudinary
                  → Stored permanently ✅
                  → Served via CDN (fast) ✅
```

## Image URLs

### Before:
```
https://ashesi-market-website-production.up.railway.app/media/products/1_None.png
```
(Broken after redeployment)

### After:
```
https://res.cloudinary.com/dxyz123abc/image/upload/v1234567890/products/1_None.png
```
(Works forever, served from CDN)

## Folder Structure on Cloudinary

Images will be organized in folders:
- `products/` - Product images
- `id_images/` - User ID verification images

## Image Transformations (Bonus!)

Cloudinary can automatically optimize images. You can add transformations:

```python
# In models.py, you can add transformations
from cloudinary.models import CloudinaryField

class Product(models.Model):
    # Instead of ImageField, use CloudinaryField for more control
    # image = CloudinaryField('image', transformation={'width': 800, 'height': 600, 'crop': 'limit'})
```

## Free Tier Limits

- Storage: 25 GB
- Bandwidth: 25 GB/month
- Transformations: 25,000/month
- Images: Unlimited

This is more than enough for your marketplace!

## Troubleshooting

### Images not uploading
- Check Railway logs for errors
- Verify environment variables are set correctly
- Check Cloudinary dashboard for API usage

### Images not showing
- Check browser console for CORS errors
- Verify image URLs in API response
- Check Cloudinary Media Library

### "Invalid credentials" error
- Double-check Cloud Name, API Key, API Secret
- Make sure no extra spaces in environment variables
- Regenerate API credentials if needed

## Current Environment Variables Summary

Your Railway Django service should now have:

```
# Database
DATABASE_URL=postgresql://...

# Django
SECRET_KEY=...
DEBUG=False
ALLOWED_HOSTS=.railway.app,.vercel.app

# CORS
CORS_ALLOWED_ORIGINS=https://ashesi-market-website.vercel.app
CSRF_TRUSTED_ORIGINS=https://ashesi-market-website.vercel.app

# Cloudinary (NEW!)
CLOUDINARY_CLOUD_NAME=your-cloud-name
CLOUDINARY_API_KEY=your-api-key
CLOUDINARY_API_SECRET=your-api-secret

# Optional: Superuser
DJANGO_SUPERUSER_EMAIL=...
DJANGO_SUPERUSER_PASSWORD=...
```

## Next Steps

1. Get Cloudinary credentials
2. Add to Railway environment variables
3. Deploy backend
4. Test image upload
5. Enjoy permanent image storage! 🎉
