from .base import *

DEBUG = False

with open('/etc/SECRET_KEY.txt') as f:
    SECRET_KEY = f.read().strip() 

with open('/etc/SQL_PASSWORD.txt') as f:
    SQL_PASSWORD = f.read().strip() 

with open('/etc/EMAIL_HOST_PASSWORD.txt') as f:
    EMAIL_HOST_PASSWORD = f.read().strip() 

ALLOWED_HOSTS += [ ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ogulcandulgerdb',
        'USER': 'ogulcandulger_admin',
        'PASSWORD': SQL_PASSWORD,
        'HOST': 'localhost'
    }
}

SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

SECURE_BROWSER_XSS_FILTER = True


CORS_ORIGIN_WHITELIST = (
)

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]
