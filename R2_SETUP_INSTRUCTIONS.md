# Cloudflare R2 Setup - Quick Instructions

## ✅ What's Already Done

1. ✅ R2 bucket created: `ashmarket`
2. ✅ Public Access enabled
3. ✅ API token created: "Backend-ashmarket"
4. ✅ Backend code updated to use R2
5. ✅ Frontend code updated to upload images with JWT

## 🔧 What You Need to Do

### Step 1: Get Your API Credentials

When you created the "Backend-ashmarket" token, Cloudflare showed you two keys:
- **Access Key ID** (looks like: `abc123def456...`)
- **Secret Access Key** (looks like: `xyz789abc...`)

⚠️ **If you closed that screen**, create a new token:
1. Go to Cloudflare → R2 → Manage R2 API Tokens
2. Click "Create API Token"
3. Name: `Backend-ashmarket-v2`
4. Permissions: Object Read & Write
5. Bucket: `ashmarket`
6. Click "Create API Token"
7. **COPY BOTH KEYS NOW** (you can't see them again!)

### Step 2: Add Environment Variables to Railway

1. Go to Railway dashboard
2. Click on your Django project
3. Click "Variables" tab
4. Add these 5 variables (click "+ New Variable" for each):

```
R2_ACCOUNT_ID=4e0271ccb020dd1603c00c7ea7fef217
R2_ACCESS_KEY_ID=<paste-your-access-key-id-here>
R2_SECRET_ACCESS_KEY=<paste-your-secret-access-key-here>
R2_BUCKET_NAME=ashmarket
R2_CUSTOM_DOMAIN=https://pub-bc50d4f6ddc648a983246d68e792aed7.r2.dev
```

**Replace:**
- `<paste-your-access-key-id-here>` → Your actual Access Key ID
- `<paste-your-secret-access-key-here>` → Your actual Secret Access Key

### Step 3: Configure CORS on R2 Bucket

1. Go to Cloudflare → R2 → Click `ashmarket` bucket
2. Click "Settings" tab
3. Scroll to "CORS Policy"
4. Click "Add CORS Policy" or "Edit"
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

### Step 4: Deploy Backend

Railway will automatically redeploy when you add the environment variables. Wait for deployment to complete (check the "Deployments" tab).

### Step 5: Test Image Upload

1. Go to `https://ashesi-market-website.vercel.app`
2. Login
3. Click "+ Sell"
4. Fill in product details
5. Upload an image
6. Click "Post Listing"
7. Check if the image appears on the product page

### Step 6: Verify in R2

1. Go to Cloudflare → R2 → `ashmarket` bucket
2. You should see a `media/` folder
3. Inside: `products/` folder with your uploaded images

## 🎯 Expected Result

After setup, images will be:
- Uploaded to: `https://4e0271ccb020dd1603c00c7ea7fef217.r2.cloudflarestorage.com/ashmarket/media/products/`
- Served from: `https://pub-bc50d4f6ddc648a983246d68e792aed7.r2.dev/media/products/`

## 🐛 Troubleshooting

### Images not uploading
- Check Railway logs for errors
- Verify all 5 environment variables are set correctly
- Make sure Access Key ID and Secret Access Key are correct

### Images not showing (404)
- Verify Public Access is enabled on R2 bucket
- Check CORS policy is configured
- Verify R2_CUSTOM_DOMAIN is correct

### CORS errors in browser console
- Make sure CORS policy includes your Vercel domain
- Check AllowedMethods includes GET and POST
- Clear browser cache and try again

## 📝 Summary

Your configuration:
- **Account ID:** `4e0271ccb020dd1603c00c7ea7fef217`
- **Bucket:** `ashmarket`
- **Public URL:** `https://pub-bc50d4f6ddc648a983246d68e792aed7.r2.dev`
- **S3 API:** `https://4e0271ccb020dd1603c00c7ea7fef217.r2.cloudflarestorage.com/ashmarket`

Just add the API credentials to Railway and you're done! 🚀
