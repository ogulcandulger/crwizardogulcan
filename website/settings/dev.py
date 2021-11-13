from .base import *
import os

SECRET_KEY =  os.getenv("SECRET_KEY")
EMAIL_HOST_PASSWORD =  os.getenv("EMAIL_HOST_PASSWORD")

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

CORS_ALLOWED_ORIGINS = (
    'http://localhost:3000',
)

CORS_ALLOW_CREDENTIALS = True
