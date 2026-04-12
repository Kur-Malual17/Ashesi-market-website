"""
Signal handlers for automatic operations
"""
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Avg, Count
from .models import User, Cart, Review


@receiver(post_save, sender=User)
def create_user_cart(sender, instance, created, **kwargs):
    """Automatically create a cart when a user is created"""
    if created:
        Cart.objects.create(user=instance)


@receiver(post_save, sender=Review)
@receiver(post_delete, sender=Review)
def update_seller_rating(sender, instance, **kwargs):
    """Update seller's average rating when reviews change"""
    seller = instance.seller
    stats = Review.objects.filter(seller=seller).aggregate(
        avg_rating=Avg('rating'),
        review_count=Count('id')
    )
    
    seller.avg_rating = stats['avg_rating'] or 0.00
    seller.review_count = stats['review_count'] or 0
    seller.save(update_fields=['avg_rating', 'review_count'])
