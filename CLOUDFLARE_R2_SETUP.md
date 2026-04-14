# Cloudflare R2 Image Storage Setup

## Why Cloudflare R2?

- ✅ **No egress fees** (free bandwidth!)
- ✅ Cheaper than S3 ($0.015/GB vs $0.023/GB)
- ✅ S3-compatible API
- ✅ Fast global CDN
- ✅ Your bucket is already created: `ashmarket`

## Step 1: Get R2 API Credentials

### 1.1 Get Account ID
1. Go to Cloudflare dashboard
2. Click "R2" in the left sidebar
3. Look at the right side - you'll see **Account ID**
4. Copy it (looks like: `abc123def456...`)

### 1.2 Create API Token
1. In R2 dashboard, click **"Manage R2 API Tokens"**
2. Click **"Create API Token"**
3. Settings:
   - **Token name:** `Django Backend`
   - **Permissions:** Select "Object Read & Write"
   - **TTL:** Leave as default (or set to never expire)
   - **Bucket:** Select `ashmarket` (or "Apply to all buckets")
4. Click **"Create API Token"**
5. **IMPORTANT:** Copy both:
   - **Access Key ID** (looks like: `abc123def456...`)
   - **Secret Access Key** (looks like: `xyz789abc...`)
   - ⚠️ Save these now - you can't see the secret again!

## Step 2: Enable Public Access

Your R2 bucket needs to be publicly accessible for images to show:

1. Go to R2 → Click `ashmarket` bucket
2. Click **"Settings"** tab
3. Under **"Public Access"**, click **"Allow Access"**
4. Confirm

Your public URL is already: `https://pub-bc50d4f6ddc648a983246d68e792aed7.r2.dev`

## Step 3: Add to Railway Environment Variables

Go to Railway → Django Service → Variables → Add these 5 variables:

```
R2_ACCOUNT_ID=4e0271ccb020dd1603c00c7ea7fef217
R2_ACCESS_KEY_ID=<PASTE_YOUR_ACCESS_KEY_ID_HERE>
R2_SECRET_ACCESS_KEY=<PASTE_YOUR_SECRET_ACCESS_KEY_HERE>
R2_BUCKET_NAME=ashmarket
R2_CUSTOM_DOMAIN=https://pub-bc50d4f6ddc648a983246d68e792aed7.r2.dev
```

**IMPORTANT:** 
- Replace `<PASTE_YOUR_ACCESS_KEY_ID_HERE>` with the Access Key ID from your "Backend-ashmarket" token
- Replace `<PASTE_YOUR_SECRET_ACCESS_KEY_HERE>` with the Secret Access Key from your "Backend-ashmarket" token
- If you closed the token creation screen, you'll need to create a new token (see Step 1.2 above)

**Your bucket details (already configured):**
- Account ID: `4e0271ccb020dd1603c00c7ea7fef217` ✅
- Bucket Name: `ashmarket` ✅
- Public URL: `https://pub-bc50d4f6ddc648a983246d68e792aed7.r2.dev` ✅
- Public Access: Enabled ✅

## Step 4: Configure CORS (Important!)

Your R2 bucket needs CORS configured so the frontend can access images:

1. Go to R2 → `ashmarket` bucket
2. Click **"Settings"** tab
3. Scroll to **"CORS Policy"**
4. Click **"Add CORS Policy"** or **"Edit"**
5. Add this configuration:

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

6. Click **"Save"**

## Step 5: Deploy Backend

```bash
cd ashesi_market_django
git add .
git commit -m "Add Cloudflare R2 image storage"
git push
```

## Step 6: Test

1. Go to your Vercel site
2. Login
3. Click "+ Sell"
4. Upload a product image
5. Submit

The image will be uploaded to R2!

## Verify Images

Check your R2 bucket:
1. Go to Cloudflare → R2 → `ashmarket`
2. You should see a `media/` folder
3. Inside: `products/` and `id_images/` folders
4. Your uploaded images!

## Image URLs

Images will be served from:
```
https://pub-bc50d4f6ddc648a983246d68e792aed7.r2.dev/media/products/1_None.png
```

## Cost Comparison

### Cloudflare R2:
- Storage: $0.015/GB/month
- **Egress: FREE** (no bandwidth charges!)
- Operations: $4.50 per million writes, $0.36 per million reads

### AWS S3:
- Storage: $0.023/GB/month
- Egress: $0.09/GB (expensive!)
- Operations: Similar

**R2 is much cheaper, especially for serving images!**

## Free Tier

R2 includes:
- 10 GB storage/month free
- No egress fees ever
- 1 million Class A operations/month free
- 10 million Class B operations/month free

Perfect for your marketplace!

## Troubleshooting

### Images not uploading
- Check Railway logs for errors
- Verify R2 credentials in Railway variables
- Check R2 bucket permissions

### Images not showing (404)
- Verify Public Access is enabled on R2 bucket
- Check CORS policy is configured
- Verify R2_CUSTOM_DOMAIN is correct

### CORS errors
- Add your Vercel domain to CORS policy
- Make sure AllowedMethods includes GET
- Check browser console for specific error

## Custom Domain (Optional)

For production, you can use a custom domain instead of the dev URL:

1. Go to R2 → `ashmarket` → Settings → Custom Domains
2. Click "Connect Domain"
3. Enter: `cdn.yourdomain.com`
4. Follow DNS setup instructions
5. Update Railway variable:
   ```
   R2_CUSTOM_DOMAIN=https://cdn.yourdomain.com
   ```

## Summary

Your setup:
- ✅ R2 bucket: `ashmarket`
- ✅ Public URL: `https://pub-bc50d4f6ddc648a983246d68e792aed7.r2.dev`
- ✅ S3-compatible API
- ✅ Free bandwidth
- ✅ Fast CDN

Just add the credentials to Railway and deploy! 🚀
