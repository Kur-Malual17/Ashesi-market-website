"""
Django settings for ashesi_market project.
"""

import os
from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='django-insecure-temp-key-for-build-only-change-in-production')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

# Warn if using default secret key in production
if not DEBUG and SECRET_KEY == 'django-insecure-temp-key-for-build-only-change-in-production':
    import sys
    print("WARNING: Using default SECRET_KEY in production! Set SECRET_KEY environment variable.", file=sys.stderr)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost,127.0.0.1,.railway.app,.vercel.app').split(',')

# Add support for wildcard subdomains
import re
class WildcardAllowedHosts(list):
    def __contains__(self, host):
        # Check exact matches first
        if super().__contains__(host):
            return True
        # Check wildcard patterns
        for pattern in self:
            if pattern.startswith('.'):
                if host.endswith(pattern) or host == pattern[1:]:
                    return True
        return False

ALLOWED_HOSTS = WildcardAllowedHosts(ALLOWED_HOSTS)

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third party
    'rest_framework',
    'corsheaders',
    'django_filters',
    
    # Local apps
    'marketplace',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ashesi_market.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'marketplace.context_processors.app_settings',
                'marketplace.context_processors.cart_count',
            ],
        },
    },
]

WSGI_APPLICATION = 'ashesi_market.wsgi.application'

# Database
# Use PostgreSQL on Railway, SQLite for local development
import dj_database_url

# Default to SQLite for local development
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Override with DATABASE_URL if provided (Railway PostgreSQL)
if 'DATABASE_URL' in os.environ:
    DATABASES['default'] = dj_database_url.config(
        conn_max_age=600,
        conn_health_checks=True,
    )
    # Optional: Add table prefix to avoid conflicts with other apps
    # DATABASES['default']['OPTIONS'] = {
    #     'options': '-c search_path=ashesi_market,public'
    # }

# MySQL Configuration (uncomment when mysqlclient is installed)
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': config('DB_NAME', default='ashesi_market'),
#         'USER': config('DB_USER', default='root'),
#         'PASSWORD': config('DB_PASSWORD', default=''),
#         'HOST': config('DB_HOST', default='localhost'),
#         'PORT': config('DB_PORT', default='3306'),
#         'OPTIONS': {
#             'charset': 'utf8mb4',
#             'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
#         },
#     }
# }

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Accra'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Media files (User uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom User Model
AUTH_USER_MODEL = 'marketplace.User'

# REST Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',  # Keep for admin panel
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
}

# JWT Settings
from datetime import timedelta
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': False,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
}

# CORS Settings
CORS_ALLOWED_ORIGINS = config(
    'CORS_ALLOWED_ORIGINS',
    default="http://localhost:3000,http://localhost:8000,http://localhost:8080,http://127.0.0.1:8080,http://127.0.0.1:5500,http://localhost:5500,https://ashesi-market-website.vercel.app"
).split(',')
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

# Session Settings
SESSION_COOKIE_AGE = 1209600  # 2 weeks
SESSION_COOKIE_HTTPONLY = True  # Secure for admin
SESSION_COOKIE_SAMESITE = 'Lax'  # Works for admin on same domain
SESSION_COOKIE_DOMAIN = None  # Allow Railway domain
SESSION_COOKIE_SECURE = config('SESSION_COOKIE_SECURE', default=False, cast=bool)
SESSION_COOKIE_PATH = '/'  # Available on all paths
SESSION_SAVE_EVERY_REQUEST = True  # Keep session alive

# CSRF Settings
CSRF_COOKIE_SAMESITE = 'Lax'  # Works for admin
CSRF_COOKIE_HTTPONLY = False  # Allow JavaScript to read CSRF token
CSRF_COOKIE_DOMAIN = None  # Allow Railway domain
CSRF_COOKIE_SECURE = config('CSRF_COOKIE_SECURE', default=False, cast=bool)
CSRF_TRUSTED_ORIGINS = config(
    'CSRF_TRUSTED_ORIGINS',
    default="http://localhost:8080,http://127.0.0.1:8080,http://127.0.0.1:5500,http://localhost:5500,https://ashesi-market-website.vercel.app"
).split(',')

# Security Settings
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True

# File Upload Settings
FILE_UPLOAD_MAX_MEMORY_SIZE = 3145728  # 3 MB
DATA_UPLOAD_MAX_MEMORY_SIZE = 3145728  # 3 MB
MAX_PRODUCT_IMAGES = 5

# App Settings
APP_NAME = 'Ashesi Market'
BASE_URL = config('BASE_URL', default='http://localhost:8000')
