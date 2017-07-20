from __future__ import absolute_import, unicode_literals

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$_ob#xrjr%l@%p*zg+6v)e=8(7un3d#bx_2k3vu6(pj_a7diqb'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# note: remove this. use some kind of kms with AWS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'travelblogdev',
        'USER': 'postgres',
        'PASSWORD': 'ChristineTravelBlogDev2017',
        'HOST': 'christinetravelblogdev.cluilm7yequg.us-east-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}


try:
    from .local import *
except ImportError:
    pass
