"""
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""
#Set the default settings module for Django

import os
#Indicates which settings file to use when running app
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'securecart.settings')

application = get_asgi_application()
