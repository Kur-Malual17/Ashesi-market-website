# 🚀 Next Steps to Enable R2 Image Storage

## Current Status
✅ Backend code updated to use R2  
✅ Frontend code updated to use JWT for image uploads  
✅ Settings configured for R2  
⏳ **Waiting for R2 credentials to be added to Railway**

---

## 📋 What You Need to Do (5 Minutes)

### Step 1: Get Your R2 API Credentials (2 min)

You created the "Backend-ashmarket" API token. You need to copy:
1. **Access Key ID** 
2. **Secret Access Key**

**If you still have the token creation screen open:**
- Copy both keys now

**If you closed the screen:**
1. Go to Cloudflare Dashboard
2. Click "R2" in sidebar
3. Click "Manage R2 API Tokens"
4. Click "Create API Token"
5. Name: `Backend-ashmarket-v2`
6. Permissions: **Object Read & Write**
7. Bucket: **ashmarket**
8. Click "Create API Token"
9. **COPY BOTH KEYS** (you can't see them again!)

---

### Step 2: Add Environment Variables to Railway (2 min)

1. Go to [Railway Dashboard](https://railway.app)
2. Click your Django project
3. Click "Variables" tab
4. Click "+ New Variable" and add each of these:

```
Variable Name: R2_ACCOUNT_ID
Value: 4e0271ccb020dd1603c00c7ea7fef217
```

```
Variable Name: R2_ACCESS_KEY_ID
Value: <paste-your-access-key-id-here>
```

```
Variable Name: R2_SECRET_ACCESS_KEY
Value: <paste-your-secret-access-key-here>
```

```
Variable Name: R2_BUCKET_NAME
Value: ashmarket
```

```
Variable Name: R2_CUSTOM_DOMAIN
Value: https://pub-bc50d4f6ddc648a983246d68e792aed7.r2.dev
```

5. Railway will automatically redeploy (wait 1-2 minutes)

---

### Step 3: Configure CORS on R2 Bucket (1 min)

1. Go to Cloudflare → R2 → Click `ashmarket` bucket
2. Click "Settings" tab
3. Scroll to "CORS Policy"
4. Click "Add CORS Policy"
5. Paste this JSON:

```json
[
  {
    "AllowedOrigins": [
      "https://ashesi-market-website.vercel.app",
      "https://*.vercel.app",
      "http://localhost:5500",
      "http://127.0.0.1:5500"
    ],
    "AllowedMethods": [
      "GET",
      "HEAD",
      "PUT",
      "POST"
    ],
    "AllowedHeaders": [
      "*"
    ],
    "ExposeHeaders": [
      "ETag"
    ],
    "MaxAgeSeconds": 3600
  }
]
```

6. Click "Save"

---

### Step 4: Test Image Upload (1 min)

1. Go to https://ashesi-market-website.vercel.app
2. Login
3. Click "+ Sell"
4. Fill in product details
5. **Upload an image**
6. Click "Post Listing"
7. ✅ Image should appear on product page!

---

### Step 5: Verify in R2 (30 sec)

1. Go to Cloudflare → R2 → `ashmarket` bucket
2. You should see:
   ```
   media/
     products/
       <your-uploaded-images>
   ```

---

## 🎯 What Will Happen

### Before (Current State):
- Products have `images: []` (empty)
- No images show on product pages
- Django admin shows no images

### After (With R2 Configured):
- Images upload to R2 when creating products
- Images show on product pages
- Django admin shows product images
- Images served from fast CDN

---

## 🔍 How to Verify It's Working

### Check Railway Logs:
1. Go to Railway → Your project → Deployments
2. Click latest deployment
3. Look for this line:
   ```
   ✅ R2 Storage configured: ashmarket
   ✅ Media URL: https://pub-bc50d4f6ddc648a983246d68e792aed7.r2.dev/media/
   ```

### Check Browser Console:
1. Open product creation page
2. Press F12 (Developer Tools)
3. Go to Console tab
4. Upload image
5. Look for:
   ```
   Image 1 uploaded successfully
   ```

### Check Product API Response:
1. Create product with image
2. Go to product detail page
3. Press F12 → Network tab
4. Refresh page
5. Click the API request
6. Look for `images` array with R2 URLs:
   ```json
   "images": [
     {
       "id": 1,
       "image": "https://pub-bc50d4f6ddc648a983246d68e792aed7.r2.dev/media/products/4_1.jpg",
       "is_primary": true
     }
   ]
   ```

---

## 🐛 Troubleshooting

### Problem: Images still not uploading

**Check:**
1. Railway logs show R2 configuration message
2. All 5 environment variables are set in Railway
3. Access Key ID and Secret Access Key are correct (no typos)
4. Railway deployment completed successfully

**Solution:**
- Redeploy Railway project
- Check Railway logs for errors
- Verify R2 credentials are correct

---

### Problem: Images upload but don't show (404)

**Check:**
1. Public Access is enabled on R2 bucket
2. CORS policy is configured
3. R2_CUSTOM_DOMAIN is correct

**Solution:**
- Go to R2 bucket → Settings → Public Access → Enable
- Add CORS policy (see Step 3)
- Clear browser cache

---

### Problem: CORS errors in browser

**Check:**
1. CORS policy includes your Vercel domain
2. AllowedMethods includes GET and POST
3. AllowedHeaders includes "*"

**Solution:**
- Update CORS policy (see Step 3)
- Make sure to save the policy
- Clear browser cache and try again

---

## 📊 Cost Estimate

### R2 Free Tier:
- 10 GB storage/month: **FREE**
- Egress (bandwidth): **FREE FOREVER**
- 1M Class A operations/month: **FREE**
- 10M Class B operations/month: **FREE**

### Your Expected Usage:
- ~100 products × 2 images × 500KB = **100 MB** (well under 10GB)
- Image views: **FREE** (no egress fees!)
- Uploads: ~200/month (well under 1M)

**Total Cost: $0.00/month** 🎉

---

## 📚 Additional Resources

- **R2 Setup Guide:** `CLOUDFLARE_R2_SETUP.md`
- **Quick Instructions:** `R2_SETUP_INSTRUCTIONS.md`
- **Fixes Applied:** `FIXES_APPLIED.md`
- **Cloudflare R2 Docs:** https://developers.cloudflare.com/r2/

---

## ✅ Checklist

Before testing:
- [ ] R2 API token created
- [ ] Access Key ID copied
- [ ] Secret Access Key copied
- [ ] 5 environment variables added to Railway
- [ ] Railway deployment completed
- [ ] CORS policy configured on R2 bucket
- [ ] Public Access enabled on R2 bucket

After testing:
- [ ] Can upload images when creating products
- [ ] Images appear on product detail pages
- [ ] Images visible in R2 bucket
- [ ] No CORS errors in browser console
- [ ] Django admin shows product images
- [ ] Railway logs show R2 configuration

---

## 🎉 Success Criteria

You'll know it's working when:
1. ✅ Create a product with an image
2. ✅ Image appears on product page
3. ✅ Image URL starts with `https://pub-bc50d4f6ddc648a983246d68e792aed7.r2.dev/`
4. ✅ Image visible in R2 bucket under `media/products/`
5. ✅ Django admin shows the image

---

**Ready? Start with Step 1! 🚀**
