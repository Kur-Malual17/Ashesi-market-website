# Registration & Login Debug Guide

## Changes Made

### Backend (views.py)
✅ Added detailed logging for registration process
✅ Added error handling with specific error messages
✅ Logs show:
  - Registration data received
  - User creation success/failure
  - Token generation
  - Validation errors

### Frontend (register.html & login.html)
✅ Added console logging for debugging
✅ Added success messages before redirect
✅ Added token validation checks
✅ Added 1-second delay to see success message
✅ Better error messages

## How to Test Registration

### Step 1: Clear Browser Storage
1. Press `F12` to open Developer Tools
2. Go to Console tab
3. Type: `localStorage.clear()`
4. Press Enter

### Step 2: Open Console
Keep Developer Tools open on the Console tab to see logs

### Step 3: Register
1. Go to register page
2. Fill in the form
3. Click "Create Account"
4. Watch the console for logs:
   ```
   Sending registration data: {...}
   Registration response: {...}
   User and tokens saved to localStorage
   ```

### Step 4: Check What Happened

**If Successful:**
- ✅ You'll see "Registration successful! Redirecting..."
- ✅ Console shows tokens received
- ✅ Redirects to homepage after 1 second
- ✅ You're logged in (see profile link in nav)

**If Failed:**
- ❌ Error message shows what went wrong
- ❌ Console shows the error
- ❌ Check Railway logs for backend errors

## How to Check if You're Logged In

### Option 1: Check localStorage
1. Press `F12`
2. Go to Application tab → Local Storage
3. Look for:
   - `access_token` (should have a long string)
   - `refresh_token` (should have a long string)
   - `user` (should have JSON with your info)

### Option 2: Check Console
```javascript
console.log('Access Token:', localStorage.getItem('access_token'));
console.log('User:', localStorage.getItem('user'));
```

### Option 3: Check Navigation
- If logged in: You'll see "Profile", "Orders", "Cart", "Sell", "Log out"
- If not logged in: You'll see "Log in", "Register"

## Common Issues & Solutions

### Issue 1: "Registration succeeded but no tokens received"
**Cause:** Backend didn't return tokens
**Solution:** Check Railway logs for backend errors

### Issue 2: Registration succeeds but can't login
**Cause:** Password not saved correctly
**Solution:** 
1. Check Railway logs
2. Try registering with a different email
3. Check if user was created in Django admin

### Issue 3: Tokens not saving
**Cause:** localStorage blocked or saveTokens function not working
**Solution:**
1. Check browser console for errors
2. Try in incognito mode
3. Check if localStorage is enabled

### Issue 4: Redirects immediately without showing success
**Cause:** Old code without delay
**Solution:** Deploy the new code with 1-second delay

## Deploy Changes

### Backend:
```bash
cd ashesi_market_django
git add .
git commit -m "Add registration and login debugging"
git push
```

### Frontend:
```bash
cd ashesi_market_frontend
git add .
git commit -m "Add registration and login success messages and debugging"
git push
```

## After Deployment - Testing Checklist

1. **Clear Storage:**
   - [ ] `localStorage.clear()` in console

2. **Test Registration:**
   - [ ] Fill registration form
   - [ ] Click "Create Account"
   - [ ] See "Registration successful!" message
   - [ ] Wait 1 second
   - [ ] Redirected to homepage
   - [ ] See profile link in navigation

3. **Test Login:**
   - [ ] Logout (if logged in)
   - [ ] Go to login page
   - [ ] Enter email and password
   - [ ] Click "Log In"
   - [ ] See "Login successful!" message
   - [ ] Wait 1 second
   - [ ] Redirected to homepage
   - [ ] See profile link in navigation

4. **Test Persistence:**
   - [ ] Refresh the page
   - [ ] Still logged in (profile link visible)
   - [ ] Close browser and reopen
   - [ ] Still logged in

5. **Test Protected Pages:**
   - [ ] Go to /profile.html - should work
   - [ ] Go to /orders.html - should work
   - [ ] Go to /cart.html - should work
   - [ ] Go to /sell.html - should work

## Check Railway Logs

To see backend logs:
1. Go to Railway dashboard
2. Click your Django service
3. Go to "Deployments" tab
4. Click latest deployment
5. Click "View Logs"

Look for:
```
Registration attempt with data: {...}
User created successfully: email@example.com
Tokens generated for user: email@example.com
```

Or errors:
```
Error creating user: ...
Validation errors: {...}
```

## If Still Not Working

1. **Check Railway logs** for backend errors
2. **Check browser console** for frontend errors
3. **Try different browser** (Chrome, Firefox, Edge)
4. **Try incognito mode** (rules out extensions)
5. **Check if email already exists** (try different email)
6. **Verify Railway environment variables** are set correctly

## Success Indicators

✅ Registration shows success message
✅ Login shows success message  
✅ Tokens saved in localStorage
✅ User data saved in localStorage
✅ Navigation shows logged-in links
✅ Can access protected pages
✅ Stays logged in after refresh
✅ Railway logs show successful user creation
