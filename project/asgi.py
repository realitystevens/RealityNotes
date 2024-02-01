import os
from django.core.asgi import get_asgi_application
from decouple import config



if config('ENV') == 'PROD':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings.production')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings.development')

application = get_asgi_application()
