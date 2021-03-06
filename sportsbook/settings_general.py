"""
Django settings for sportsbook project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import django.conf.global_settings as DEFAULT_SETTINGS
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django_forms_bootstrap',
    'bootstrapform',
    'django_extensions',
    'registration',
    'south',
    'management',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS+("django.core.context_processors.request","django.contrib.messages.context_processors.messages")

ROOT_URLCONF = 'sportsbook.urls'

WSGI_APPLICATION = 'sportsbook.wsgi.application'

AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',)

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# # Registration
# ACCOUNT_ACTIVATION_DAYS=7
# EMAIL_HOST='localhost'
# EMAIL_PORT= 1023
# EMAIL_HOST_USER='username'
# EMAIL_HOST_PASSWORD='password'
TIME_INPUT_FORMATS = (
    '%I%p',
    '%I %p',
    '%I:%M%p',
    '%I:%M %p',
)
