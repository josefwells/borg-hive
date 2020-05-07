"""
Django settings for borghive project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import socket

from django.contrib.messages import constants as message_constants
from environs import Env

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env = Env()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY', '++apz(*cojac+1u$io&w)wg^r5vgaon%@wvpd#@j5iv9!9#lsg')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', True)

ALLOWED_HOSTS = ['localhost', socket.getfqdn()]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django_extensions',
    'django_celery_beat',
    'crispy_forms',
    'borghive'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'login_required.middleware.LoginRequiredMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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
CRISPY_TEMPLATE_PACK = 'bootstrap4'

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('MYSQL_DATABASE', 'borghive'),
        'USER': env('MYSQL_USER', 'borghive'),
        'PASSWORD': env('MYSQL_PASSWORD', 'borghive'),
        'HOST': env('MYSQL_HOST', 'db'),
        'PORT': env.int('MYSQL_PORT', 3306)
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
LOGIN_REDIRECT_URL = '/'
LOGIN_REQUIRED_IGNORE_VIEW_NAMES = [
    'login',
    'admin:login',
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'de-de'

TIME_ZONE = 'Europe/Zurich'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/static'
STATICFILES_DIRS = ['static']

#
# Celery
#
CELERY_TASK_ALWAYS_EAGER = env.bool('CELERY_TASK_ALWAYS_EAGER', False)
CELERY_BROKER_URL = env('CELERY_BROKER_URL', 'redis://redis:6379/0')
CELERY_RESULT_BACKEND = env('CELERY_RESULT_BACKEND','redis://redis:6379/0')


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': env('DJANGO_LOG_LEVEL', 'INFO')
        },
        'borghive': {
            'handlers': ['console'],
            'propagate': True,
            'level': env('APP_LOG_LEVEL', 'DEBUG')
        },
    },
}

MESSAGE_TAGS = {
    message_constants.ERROR: 'danger',
}

handler404 = 'borghive.views.error.error404'
handler500 = 'borghive.views.error.error505'



#
# APP
#
BORGHIVE = {
    'REPO_PATH': env("BORGHIVE_REPO_PATH", '/repos'),
    'LOGIN_CONFIG_PATH': env('LOGIN_CONFIG_PATH', '/config'),
    'SSH_PUBLIC_KEY_REGEX': 'ssh-([a-zA-Z0-9]+) (AAAA[0-9A-Za-z+/=]+)( [\w\-@]+)?'
}

#
# NOTIFICATION SETTINGS
#
EMAIL_HOST = env('EMAIL_HOST', 'localhost')
EMAIL_PORT = env('EMAIL_PORT', '465')
EMAIL_HOST_USER = env('EMAIL_HOST_USER', 'root')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', 'password')
EMAIL_USE_TLS = True  # disallow unsecure communication!
EMAIL_FROM = env('EMAIL_FROM', 'borghive@{}'.format(socket.getfqdn()))
if DEBUG: EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
