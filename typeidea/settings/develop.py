from .base import *  # NOQA


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
