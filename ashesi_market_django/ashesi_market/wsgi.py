"""
WSGI config for ashesi_market project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ashesi_market.settings')

application = get_wsgi_application()
