"""
One-time script to create superuser
Run this once, then delete it
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ashesi_market.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Change these values
EMAIL = 'admin@ashesi.edu.gh'
PASSWORD = 'admin123'  # Change this!
FIRST_NAME = 'Admin'
LAST_NAME = 'User'

if not User.objects.filter(email=EMAIL).exists():
    User.objects.create_superuser(
        email=EMAIL,
        password=PASSWORD,
        first_name=FIRST_NAME,
        last_name=LAST_NAME,
        phone_whatsapp='0000000000',
        year_group=2024,
        role='admin'
    )
    print(f'Superuser created: {EMAIL}')
else:
    print(f'User {EMAIL} already exists')
