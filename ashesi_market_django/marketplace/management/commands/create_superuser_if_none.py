"""
Management command to create a superuser from environment variables
Usage: python manage.py create_superuser_if_none
"""
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from decouple import config

User = get_user_model()


class Command(BaseCommand):
    help = 'Create a superuser from environment variables if no superuser exists'

    def handle(self, *args, **options):
        # Check if any superuser exists
        if User.objects.filter(is_superuser=True).exists():
            self.stdout.write(self.style.WARNING('Superuser already exists. Skipping creation.'))
            return

        # Get credentials from environment variables
        email = config('DJANGO_SUPERUSER_EMAIL', default=None)
        password = config('DJANGO_SUPERUSER_PASSWORD', default=None)
        first_name = config('DJANGO_SUPERUSER_FIRST_NAME', default='Admin')
        last_name = config('DJANGO_SUPERUSER_LAST_NAME', default='User')

        if not email or not password:
            self.stdout.write(
                self.style.WARNING(
                    'DJANGO_SUPERUSER_EMAIL and DJANGO_SUPERUSER_PASSWORD '
                    'environment variables not set. Skipping superuser creation.'
                )
            )
            return

        # Create superuser
        try:
            # Generate username from email
            username = email.split('@')[0]
            
            user = User.objects.create_superuser(
                email=email,
                username=username,
                password=password,
                first_name=first_name,
                last_name=last_name,
                phone_whatsapp='0000000000',  # Default phone
                year_group='2024',  # Default year
                role='both'  # Admin can be both buyer and seller
            )
            self.stdout.write(
                self.style.SUCCESS(f'Superuser created successfully: {email}')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error creating superuser: {str(e)}')
            )
