# Fixes Applied for R2 Image Upload

## Date: April 14, 2026

## Issues Identified

1. ❌ Images not being uploaded to R2 (empty `images: []` array)
2. ❌ Frontend using CSRF tokens instead of JWT for image uploads
3. ❌ R2 credentials not configured in Railway
4. ❌ CORS policy not configured on R2 bucket
5. ❌ Settings.py had duplicate MEDIA_URL/MEDIA_ROOT definitions

## Fixes Applied

### 1. Fixed Frontend Image Upload (sell.html)
**Changed:** Image upload now uses JWT authentication instead of CSRF tokens

**Before:**
```javascript
headers: {
    'X-CSRFToken': csrfToken
}
```

**After:**
```javascript
headers: {
    'Authorization': `Bearer ${token}`
}
```

**Why:** The backend uses JWT authentication, not session-based auth. CSRF tokens don't work with JWT.

### 2. Fixed Django Settings (settings.py)
**Changed:** Removed duplicate MEDIA_URL/MEDIA_ROOT definitions and added debug logging

**Before:**
- Had duplicate media settings (one for R2, one for local)
- No logging to verify R2 configuration

**After:**
- Single conditional media configuration
- Prints confirmation when R2 is configured
- Properly sets MEDIA_ROOT to None when using R2

**Why:** Duplicate definitions caused confusion and local storage to override R2 settings.

### 3. Updated R2 Setup Documentation
**Files Updated:**
- `CLOUDFLARE_R2_SETUP.md` - Updated with your exact credentials
- `R2_SETUP_INSTRUCTIONS.md` - Created quick reference guide

**Your R2 Details:**
- Account ID: `4e0271ccb020dd1603c00c7ea7fef217`
- Bucket: `ashmarket`
- Public URL: `https://pub-bc50d4f6ddc648a983246d68e792aed7.r2.dev`
- S3 API: `https://4e0271ccb020dd1603c00c7ea7fef217.r2.cloudflarestorage.com/ashmarket`

## What You Need to Do Now

### ✅ Step 1: Get Your API Keys
You created the "Backend-ashmarket" token. You need:
- Access Key ID
- Secret Access Key

If you don't have them, create a new token (see R2_SETUP_INSTRUCTIONS.md)

### ✅ Step 2: Add to Railway
Add these 5 environment variables:
```
R2_ACCOUNT_ID=4e0271ccb020dd1603c00c7ea7fef217
R2_ACCESS_KEY_ID=<your-access-key-id>
R2_SECRET_ACCESS_KEY=<your-secret-access-key>
R2_BUCKET_NAME=ashmarket
R2_CUSTOM_DOMAIN=https://pub-bc50d4f6ddc648a983246d68e792aed7.r2.dev
```

### ✅ Step 3: Configure CORS on R2
Add CORS policy to your R2 bucket (see R2_SETUP_INSTRUCTIONS.md for JSON)

### ✅ Step 4: Deploy
Push changes to Railway:
```bash
cd ashesi_market_django
git add .
git commit -m "Fix R2 image upload with JWT authentication"
git push
```

### ✅ Step 5: Test
1. Go to Vercel site
2. Login
3. Create a product with an image
4. Verify image appears on product page
5. Check R2 bucket for uploaded files

## How Image Upload Works Now

### Frontend Flow:
1. User fills product form and selects images
2. Frontend creates product via POST `/api/products/`
3. For each image:
   - Creates FormData with image file
   - Sends POST to `/api/products/{id}/upload_image/`
   - **Uses JWT token in Authorization header**
4. Backend saves image to R2
5. Image URL returned: `https://pub-bc50d4f6ddc648a983246d68e792aed7.r2.dev/media/products/4_1.jpg`

### Backend Flow:
1. Receives image upload request
2. Validates JWT token
3. Checks user is product owner
4. Checks max 5 images limit
5. Saves image to R2 using boto3
6. Returns ProductImage object with R2 URL

## Expected Results

### In Django Admin:
- Product should show "Product images" section
- Can add/remove images
- Can set primary image

### On Frontend:
- Product detail page shows images
- Product list shows primary image
- Images load from R2 CDN

### In R2 Bucket:
```
ashmarket/
  media/
    products/
      4_1.jpg
      4_2.jpg
    id_images/
      10_id.png
```

## Verification Checklist

After deploying:
- [ ] Railway logs show "✅ R2 Storage configured: ashmarket"
- [ ] Can create product with images on Vercel site
- [ ] Images appear on product detail page
- [ ] Images visible in R2 bucket
- [ ] No CORS errors in browser console
- [ ] Django admin shows product images

## Troubleshooting

### Images still not uploading
- Check Railway logs for R2 configuration message
- Verify all 5 environment variables are set
- Check Access Key ID and Secret Access Key are correct

### Images upload but don't show
- Verify Public Access is enabled on R2 bucket
- Check CORS policy is configured
- Clear browser cache

### 403 Forbidden errors
- Check JWT token is valid
- Verify user is logged in
- Check user owns the product

## Files Modified

1. `ashesi_market_frontend/sell.html` - Fixed JWT auth for image upload
2. `ashesi_market_django/ashesi_market/settings.py` - Fixed R2 configuration
3. `CLOUDFLARE_R2_SETUP.md` - Updated with your credentials
4. `R2_SETUP_INSTRUCTIONS.md` - Created quick reference
5. `FIXES_APPLIED.md` - This file

## Next Steps

Once R2 is working:
1. Test uploading multiple images
2. Test editing products and changing images
3. Test deleting images
4. Monitor R2 usage in Cloudflare dashboard
5. Consider adding image compression/resizing

## Support

If you encounter issues:
1. Check Railway deployment logs
2. Check browser console for errors
3. Verify R2 credentials in Railway
4. Check CORS policy in R2 bucket
5. Test with a simple image upload first

---

**Status:** ✅ Code fixes applied, waiting for R2 credentials to be added to Railway
