"""
Signal handlers for automatic operations
"""
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Cart


@receiver(post_save, sender=User)
def create_user_cart(sender, instance, created, **kwargs):
    """Automatically create a cart when a user is created"""
    if created:
        Cart.objects.create(user=instance)

