import os

from pathlib import Path

from django.utils.translation import ugettext_lazy as _

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-^7=9e#u#r@7kl@rg(976t5%kam#+7(d)sazhvqad5@-$mk5=b+'

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATICFILES_DIRS = [
    BASE_DIR / 'teachers/static', 
    BASE_DIR / 'main/static',
]