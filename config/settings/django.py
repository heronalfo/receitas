import os

DEBUG = False if os.environ.get('DEBUG', "1") == "0" else True

ALLOWED_HOSTS = []

ROOT_URLCONF = 'config.urls'

INTERNAL_IPS = [ "127.0.0.1", ]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

WSGI_APPLICATION = 'config.wsgi.application'