import os

from pathlib import Path

from django.utils.translation import ugettext_lazy as _

BASE_DIR = Path(__file__).resolve().parent.parent


DEBUG = False

ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': BASE_DIR / 'db.sqlite3',
        'USER': 'postgres',
        'PASSWORD': 123,
        'HOST': 'localhost',
        'PORT': 5432
    }
}


SECRET_KEY = 'django-insecure-^7125768lgdmwkl@rg(976t5%kam#+7(d)sazhvqad5@-$mk5=b+'

STATICFILES_DIRS = [
    BASE_DIR / 'teachers/static', 
    BASE_DIR / 'main/static',
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')