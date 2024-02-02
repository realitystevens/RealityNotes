from decouple import config
from project.settings.settings import *
import cloudinary
import cloudinary.api
import cloudinary.uploader


DEBUG = False

ALLOWED_HOSTS = [
    '.onrender.com',
    'n.realitystevens.me'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config('CLOUDINARY_CLOUDNAME'),
    'API_KEY': config('CLOUDINARY_APIKEY'),
    'API_SECRET': config('CLOUDINARY_APISECRET'),
}

cloudinary.config(
    cloud_name=config('CLOUDINARY_CLOUDNAME'),
    api_key=config('CLOUDINARY_APIKEY'),
    api_secret=config('CLOUDINARY_APISECRET'),
)

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
    }
}

CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
