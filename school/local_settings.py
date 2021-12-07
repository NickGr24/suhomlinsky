import os

from pathlib import Path

from django.utils.translation import ugettext_lazy as _

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-^7=9e#u#r@7kl@rg(976t5%kam#+7(d)sazhvqad5@-$mk5=b+'

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'school',
        'USER': 'nikita',
        'PASSWORD': '12',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

STATICFILES_DIRS = [
    BASE_DIR / 'main/static',
]


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR / 'media')