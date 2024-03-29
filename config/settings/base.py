"""
Django settings for epsilonpos_backend project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path
import json
import pymysql

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Static files (CSS, JavaScript, images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '../static/')  # Update this path based on your project structure

# Additional locations of static files
STATICFILES_DIRS = [
    # os.path.join(BASE_DIR, '/static/'),  # Add other paths if necessary
]

# Media files (uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '/media/') 

pymysql.install_as_MySQLdb()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-nx=0fe@+bw$e1-&x&)ys!yvrvexw2b3m-(e%d__hb2$wh%hzwn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ROOT_URLCONF = 'epsilonpos_backend.urls'

ALLOWED_HOSTS = ['localhost', 'test.epsilonpos.com']
CORS_ORIGIN_ALLOW_ALL = True


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.IsAdminUser',
    ),
}
# Application definition

JWT_AUTH = {
    # Authorization:Token xxx
    'JWT_AUTH_HEADER_PREFIX': 'Token',
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
    'corsheaders',
    'constance',
    'djmoney',
    'phonenumber_field',
    'django_extensions',
    'apps.accounts',
    'apps.stock',
    'apps.pos',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases



AUTH_USER_MODEL = 'accounts.CustomUser' #Changes default User to CustomUser

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


tnm_mpamba_file = Path(BASE_DIR, 'service_fees/tnm_mpamba.json'),
airtel_money_file = Path(BASE_DIR, 'service_fees/airtel_money.json'),



# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CONSTANCE_ADDITIONAL_FIELDS = {
'image_field': ['django.forms.ImageField', {}],
'float_field': ['django.forms.FloatField', {}],
'boolean_field': ['django.forms.BooleanField', {}],
'yes_no_null_select': ['django.forms.fields.ChoiceField', {'widget': 'django.forms.Select','choices': (("yes", "Yes"), ("no", "No"))
}],
}

# Load payment_options.json content
payment_options_file = Path(BASE_DIR, 'payments/payment_options.json')

with open(payment_options_file, 'r') as file:
    payment_options_data = json.load(file)
    

# Extract payment options
payment_options = payment_options_data.get("payment_options", [])

# Load tnm_mpamba_file content
with open(tnm_mpamba_file[0], 'r') as file:
    tnm_mpamba_data = json.load(file)

# Extract cash_out_fees from tnm_mpamba_data
tnm_mpamba_fees = tnm_mpamba_data.get("tnm_mpamba", {}).get("cash_out_fees", [])

# Convert "from" and "to" values to integers
for fee in tnm_mpamba_fees:
    fee["from"] = int(fee["from"])
    fee["to"] = int(fee["to"])

# Load airtel_money_file content
with open(airtel_money_file[0], 'r') as file:
    airtel_money_data = json.load(file)

# Extract cash_out_fees from airtel_money_data
airtel_money_fees = airtel_money_data.get("airtel_money", {}).get("cash_out_fees", [])

# Convert "from" and "to" values to integers
for fee in airtel_money_fees:
    fee["from"] = int(fee["from"])
    fee["to"] = int(fee["to"])


CONSTANCE_CONFIG = {

'SHOP_NAME':('EPSILON BAR','You are Home!!' ),
'TAG_LINE':('The best in Town!!', 'The best Shop in Town'),
'ADDRESS':('P.O. Box 418','Address' ),
'LOCATION':('Lilongwe','Lilongwe' ),
'COUNTRY':('Malawi','Malawi' ),
'TEL':('+ 265 000 000',' Tel'),
'FAX':('+ 265 000 000',' Fax'),
'CEL':('+ 265 000 000',' Cel'),
'EMAIL':('mcatechmw@mcatech.mw','MCATECH'),
'LOGO_IMAGE': ('images.png', 'Company logo', 'image_field'),
'USE_VAT': (True, 'Use VAT', 'boolean_field'),  # Checkbox to enable/disable VAT
# VAT rate, only visible if 'USE_VAT' is checked
'VAT_RATE': (16.5, 'VAT Rate', 'float_field', {'depends': ['USE_VAT']}),

'MULTIPLE_PAYMENTS': ('yes', 'Use multiple Payments Options', 'yes_no_null_select'), 


**{
        f'ABTN_{fee["from"]}_{fee["to"]}': (
            float(fee["fee"]),
            f'From MWK {fee["from"]} to MWK {fee["to"]}',
            'float_field'
        ) for fee in airtel_money_fees
    },
**{
        f'MBTN_{fee["from"]}_{fee["to"]}': (
            float(fee["fee"]),
            f'From MWK {fee["from"]} to MWK {fee["to"]}',
            'float_field'
        ) for fee in tnm_mpamba_fees
    },
**{
    f'{option["name"]}': (
        float(option.get("fee", 0.0)),  # Use get() to handle missing 'fee' key
        f'{option.get("name", "Unknown")} Fee',  # Use get() to handle missing 'name' key
        'float_field'
    ) for option in payment_options
},


'ACCOUNT_NUMBER':('1234567890','ACCOUNT NUMBER'),
'QUICK_SALE': ('yes', 'QUICK_SALE', 'yes_no_null_select'),
}

CONSTANCE_CONFIG_FIELDSETS = {
'Mpamba Fees': {
        'fields': [f'MBTN_{fee["from"]}_{fee["to"]}' for fee in tnm_mpamba_fees],
    },
'Airtel Money Fees': {
        'fields': [f'ABTN_{fee["from"]}_{fee["to"]}' for fee in airtel_money_fees],
    },
'Payment Options': [
        f'{option["name"]}' for option in payment_options
    ],
'Shop Options': ('SHOP_NAME','LOGO_IMAGE','TAG_LINE','ADDRESS','LOCATION','TEL','FAX','EMAIL','CEL','COUNTRY'),
'Invoice Options': ('USE_VAT','VAT_RATE'),
'Pos Settings':('QUICK_SALE','ACCOUNT_NUMBER','MULTIPLE_PAYMENTS'),

}
