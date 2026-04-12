# JWT Token Expiry Fix

## Problem
You're seeing "User not found" 401 errors because you have old/invalid JWT tokens in your browser's localStorage from before we implemented JWT authentication.

## Quick Fix (For You Right Now)

### Option 1: Clear Browser Storage Manually
1. Open your site: https://ashesi-market-website.vercel.app
2. Press `F12` to open Developer Tools
3. Go to "Application" tab (Chrome) or "Storage" tab (Firefox)
4. Click "Local Storage" → Your domain
5. Click "Clear All" or delete these items:
   - `access_token`
   - `refresh_token`
   - `user`
6. Refresh the page

### Option 2: Use the Clear Storage Page
1. Go to: https://ashesi-market-website.vercel.app/clear-storage.html
2. Click "Clear Storage & Reload"
3. Done!

### Option 3: Use Browser Console
1. Press `F12` to open Developer Tools
2. Go to "Console" tab
3. Type: `localStorage.clear()`
4. Press Enter
5. Refresh the page

## What I Fixed in the Code

### Frontend (api.js)
✅ Added automatic token cleanup on 401 errors
✅ Clears invalid tokens automatically
✅ Redirects to login only for protected pages
✅ Allows anonymous browsing even with expired tokens

### Frontend (auth.js)
✅ Better token validation
✅ Clears user data if token is missing

### Created clear-storage.html
✅ Easy way for users to clear storage
✅ Can be accessed at: `/clear-storage.html`

## Deploy Changes

```bash
cd ashesi_market_frontend
git add .
git commit -m "Fix JWT token expiry handling and add storage clear page"
git push
```

## After Deployment

1. **Clear your browser storage** (use one of the 3 options above)
2. **Refresh the page** - you should see products now!
3. **Register/Login** - you'll get fresh tokens
4. **Everything should work!**

## How It Works Now

### Anonymous Users (Not Logged In):
- ✅ Can view products
- ✅ Can view categories
- ✅ Can search
- ❌ Cannot add to cart
- ❌ Cannot create listings

### Logged In Users:
- ✅ All anonymous features
- ✅ Can add to cart
- ✅ Can create listings
- ✅ Can view orders
- ✅ Can edit profile

### Token Expiry:
- Access token expires: 60 minutes
- Refresh token expires: 7 days
- When expired: Automatically cleared
- User redirected to login only if accessing protected pages

## Testing

After clearing storage and redeploying:

1. **Test Anonymous Access:**
   - [ ] Visit homepage - should see products
   - [ ] View product details - should work
   - [ ] Search products - should work

2. **Test Login:**
   - [ ] Register new account - should work
   - [ ] Login - should work
   - [ ] View profile - should work
   - [ ] Add to cart - should work

3. **Test Token Expiry:**
   - [ ] Wait 60 minutes (or manually delete access_token)
   - [ ] Try to access cart - should redirect to login
   - [ ] Homepage should still work

## For Other Users

If other users experience this issue, tell them to:
1. Visit: `https://ashesi-market-website.vercel.app/clear-storage.html`
2. Click "Clear Storage & Reload"
3. Done!

Or add this to your FAQ/Help section.
