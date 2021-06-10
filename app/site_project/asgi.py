"""
ASGI config for site_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
import django
from channels.routing import get_default_application
from channels.layers import get_channel_layer


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'site_project.settings')
django.setup()

# Application
application = get_default_application()

# Layers
channel_layer = get_channel_layer()
