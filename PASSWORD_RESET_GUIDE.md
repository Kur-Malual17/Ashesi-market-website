# Password Reset Implementation Guide

## ✅ **Features Implemented**

1. **Forgot Password** - User requests password reset via email
2. **Reset Password** - User clicks email link and sets new password
3. **Change Password** - Logged-in user can change password

---

## 📋 **API Endpoints**

### **1. Request Password Reset**

**URL**: `POST /api/auth/password-reset/request/`

**Authentication**: None required

**Request Body**:
```json
{
    "email": "user@ashesi.edu.gh"
}
```

**Response** (`200 OK`):
```json
{
    "message": "If an account exists with this email, you will receive a password reset link.",
    "email": "user@ashesi.edu.gh"
}
```

**Note**: Always returns 200 for security (doesn't reveal if email exists)

---

### **2. Reset Password with Token**

**URL**: `POST /api/auth/password-reset/confirm/`

**Authentication**: None required

**Request Body**:
```json
{
    "token": "abc123-token-from-email",
    "uid": "5",
    "new_password": "newsecurepass123",
    "confirm_password": "newsecurepass123"
}
```

**Response** (`200 OK`):
```json
{
    "message": "Password reset successful. You can now login with your new password."
}
```

**Error** (`400 Bad Request`):
```json
{
    "error": "Invalid or expired reset link"
}
```

---

### **3. Change Password (Logged-in User)**

**URL**: `POST /api/auth/password-change/`

**Authentication**: Required (Bearer token)

**Request Body**:
```json
{
    "current_password": "oldpassword123",
    "new_password": "newpassword123",
    "confirm_password": "newpassword123"
}
```

**Response** (`200 OK`):
```json
{
    "message": "Password changed successfully"
}
```

**Error** (`400 Bad Request`):
```json
{
    "error": "Current password is incorrect"
}
```

---

## 🌐 **Frontend Pages**

### **1. Forgot Password Page**
**URL**: `https://ashesi-market-website.vercel.app/forgot-password.html`

**Features**:
- Email input field
- Sends reset request to API
- Shows success message
- Redirects to login after 5 seconds

---

### **2. Reset Password Page**
**URL**: `https://ashesi-market-website.vercel.app/reset-password.html?token=XXX&uid=5`

**Features**:
- Gets token and uid from URL parameters
- New password input (min 8 characters)
- Confirm password input
- Validates passwords match
- Redirects to login after success

---

### **3. Change Password Page**
**URL**: `https://ashesi-market-website.vercel.app/change-password.html`

**Features**:
- Requires login
- Current password verification
- New password input
- Confirm password input
- Redirects to profile after success

---

### **4. Login Page Updated**
**URL**: `https://ashesi-market-website.vercel.app/login.html`

**Added**:
- "Forgot Password?" link above login button

---

## 📧 **Email Configuration**

### **For Development (Console Backend)**

Emails print to console/logs. No configuration needed.

**Current Setting**:
```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

---

### **For Production (Gmail SMTP)**

Add these environment variables to Railway:

```env
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
DEFAULT_FROM_EMAIL=noreply@ashesimarket.com
```

**How to get Gmail App Password**:
1. Go to Google Account settings
2. Security → 2-Step Verification
3. App passwords → Generate new
4. Copy the 16-character password
5. Use it as `EMAIL_HOST_PASSWORD`

---

### **Alternative: SendGrid (Recommended for Production)**

```env
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.sendgrid.net
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=apikey
EMAIL_HOST_PASSWORD=your-sendgrid-api-key
DEFAULT_FROM_EMAIL=noreply@ashesimarket.com
```

---

## 🧪 **Testing on Postman**

### **Test 1: Request Password Reset**

**Request**:
```
POST https://ashesi-market-website-production.up.railway.app/api/auth/password-reset/request/

Headers:
Content-Type: application/json

Body:
{
    "email": "testuser@ashesi.edu.gh"
}
```

**Expected**: `200 OK` with success message

**Check**: Console logs (development) or email inbox (production)

---

### **Test 2: Reset Password**

**Request**:
```
POST https://ashesi-market-website-production.up.railway.app/api/auth/password-reset/confirm/

Headers:
Content-Type: application/json

Body:
{
    "token": "TOKEN_FROM_EMAIL",
    "uid": "USER_ID_FROM_EMAIL",
    "new_password": "newpass123",
    "confirm_password": "newpass123"
}
```

**Expected**: `200 OK` with success message

---

### **Test 3: Change Password**

**Request**:
```
POST https://ashesi-market-website-production.up.railway.app/api/auth/password-change/

Headers:
Content-Type: application/json
Authorization: Bearer YOUR_ACCESS_TOKEN

Body:
{
    "current_password": "oldpass123",
    "new_password": "newpass123",
    "confirm_password": "newpass123"
}
```

**Expected**: `200 OK` with success message

---

## 🔒 **Security Features**

1. **Token Expiry**: Reset tokens expire after 24 hours
2. **One-time Use**: Tokens are invalidated after password reset
3. **No Email Enumeration**: Always returns success message (doesn't reveal if email exists)
4. **Password Validation**: Minimum 8 characters required
5. **Current Password Check**: Change password requires current password
6. **HTTPS Only**: All requests over secure connection

---

## 🚀 **Deployment Steps**

### **1. Commit Backend Changes**
```bash
cd ashesi_market_django
git add marketplace/views.py marketplace/urls.py ashesi_market/settings.py
git commit -m "Add password reset functionality"
git push
```

### **2. Commit Frontend Changes**
```bash
cd ashesi_market_frontend
git add forgot-password.html reset-password.html change-password.html login.html
git commit -m "Add password reset pages"
git push
```

### **3. Configure Email on Railway**

Add environment variables (see Email Configuration section above)

### **4. Test**

1. Visit `https://ashesi-market-website.vercel.app/login.html`
2. Click "Forgot Password?"
3. Enter email
4. Check console logs (dev) or email (prod)
5. Click reset link
6. Set new password
7. Login with new password

---

## 📊 **User Flow**

### **Forgot Password Flow**:
```
1. User clicks "Forgot Password?" on login page
2. User enters email address
3. System sends reset email (or logs to console)
4. User clicks link in email
5. User enters new password
6. User logs in with new password
```

### **Change Password Flow**:
```
1. Logged-in user goes to profile
2. User clicks "Change Password"
3. User enters current password
4. User enters new password
5. User confirms new password
6. Password updated
7. User continues using account
```

---

## ✅ **Testing Checklist**

- [ ] Request password reset with valid email
- [ ] Request password reset with invalid email (should still return success)
- [ ] Click reset link from email
- [ ] Reset password with matching passwords
- [ ] Reset password with non-matching passwords (should fail)
- [ ] Reset password with expired token (should fail)
- [ ] Change password while logged in
- [ ] Change password with wrong current password (should fail)
- [ ] Login with new password after reset
- [ ] "Forgot Password?" link visible on login page

---

## 🐛 **Troubleshooting**

### **Email not sending**
- Check EMAIL_HOST_USER and EMAIL_HOST_PASSWORD are set
- Check Gmail app password is correct
- Check EMAIL_BACKEND is set to SMTP backend
- Check Railway logs for email errors

### **Reset link not working**
- Check token and uid are in URL
- Check token hasn't expired (24 hours)
- Check user ID exists in database

### **Change password fails**
- Check user is logged in (has valid token)
- Check current password is correct
- Check new password meets requirements (8+ characters)

---

## 📝 **Future Enhancements**

1. **Email Templates**: HTML email templates with branding
2. **Rate Limiting**: Limit password reset requests per IP
3. **Password Strength Meter**: Visual indicator on frontend
4. **Password History**: Prevent reusing recent passwords
5. **2FA**: Two-factor authentication option
6. **Account Lockout**: Lock account after failed attempts

---

**Status**: ✅ Implemented and Ready for Testing  
**Date**: April 30, 2026  
**Version**: 1.0
