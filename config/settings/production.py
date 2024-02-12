from .base import *


# STATIC_URL = '/static/'
# STATIC_ROOT = '/var/www/epsilonposv2/epsilonpos_backend/config/static/'

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'epsilonpos_backend/config/static'),
#     # Other paths...
# ]

# Media settings
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'epsilonpos',
        'USER': 'root',
        'PASSWORD': 'michelle@2018',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

