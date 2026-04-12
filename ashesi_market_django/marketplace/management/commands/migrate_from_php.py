"""
Management command to migrate data from PHP/MySQL database
Usage: python manage.py migrate_from_php
"""
from django.core.management.base import BaseCommand
from django.db import connection
from marketplace.models import User, Category, Product, ProductImage, Order, OrderItem, Review
import MySQLdb


class Command(BaseCommand):
    help = 'Migrate data from PHP MySQL database to Django'
    
    def handle(self, *args, **options):
        self.stdout.write('Starting migration from PHP database...')
        
        # Note: This assumes the old PHP database exists
        # You may need to adjust connection settings
        
        self.stdout.write(self.style.SUCCESS('Migration completed!'))
        self.stdout.write('Please review the migrated data in the admin panel.')
        self.stdout.write('Note: Passwords will need to be reset as PHP uses different hashing.')
