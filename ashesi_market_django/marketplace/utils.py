"""
Utility functions for Ashesi Market
"""
import re
from urllib.parse import quote


def format_whatsapp_number(phone):
    """
    Format phone number for WhatsApp
    Strip non-digits, assume Ghanaian +233 if no country code
    """
    if not phone:
        return None
    
    # Remove all non-digit characters
    phone = re.sub(r'\D', '', phone)
    
    # If starts with 0 and is 10 digits, assume Ghana
    if len(phone) == 10 and phone[0] == '0':
        phone = '233' + phone[1:]
    
    return phone


def whatsapp_url(phone, message):
    """
    Generate WhatsApp URL with pre-filled message
    """
    formatted_phone = format_whatsapp_number(phone)
    if not formatted_phone:
        return None
    
    encoded_message = quote(message)
    return f"https://wa.me/{formatted_phone}?text={encoded_message}"


def get_star_rating_html(rating, max_stars=5):
    """
    Generate HTML for star rating display
    """
    filled = int(round(rating))
    stars = []
    
    for i in range(1, max_stars + 1):
        if i <= filled:
            stars.append('<span class="star filled">★</span>')
        else:
            stars.append('<span class="star">☆</span>')
    
    return ''.join(stars)
