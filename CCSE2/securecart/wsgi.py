
import os

from django.core.wsgi import get_wsgi_application

#Indicates to Django which settings file to use when starting the application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'securecart.settings')

application = get_wsgi_application()
