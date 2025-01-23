import os
from django.core.wsgi import get_wsgi_application
from decouple import config



if config('ENV') == 'PROD':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings.production')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings.development')

application = get_wsgi_application()
app = application
