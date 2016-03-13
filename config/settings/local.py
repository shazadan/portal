from .base import *

DEBUG = True

ADMINS = (('Admin', get_env_variable('DEFAULT_FROM_EMAIL')),)
MANAGERS = ADMINS

# EMAIL CONFIGURATION
# ===================
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = get_env_variable('EMAIL_HOST')
EMAIL_HOST_USER = get_env_variable('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = get_env_variable('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL = get_env_variable('DEFAULT_FROM_EMAIL')

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': get_env_variable('DB_NAME'),
#        'USER': get_env_variable('DB_USER'),
#        'PASSWORD': get_env_variable('DB_PASSWORD'),
#        'HOST': get_env_variable('DB_HOST'),
#        'PORT': get_env_variable('DB_PORT'),
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

INSTALLED_APPS += ('debug_toolbar',)