"""
Django settings for finance project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

from django.core.urlresolvers import reverse_lazy

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from finance.settings import secret

SETTINGS_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# BASE_DIR (where manage.py is) is ine folder up, than settings dir
BASE_DIR = os.path.abspath(os.path.join(SETTINGS_DIR, os.pardir))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

SECRET_KEY = secret.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['localhost', '188.166.117.76',
                 'finantious.com', 'www.finantious.com']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'books',
    'finance',
    'opbeat.contrib.django',
    'pipeline',
    'widget_tweaks',
)

MIDDLEWARE_CLASSES = (
    'opbeat.contrib.django.middleware.OpbeatAPMMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'finance.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['finance/templates'],
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

WSGI_APPLICATION = 'finance.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'finance',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Vilnius'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# redirect after login
LOGIN_REDIRECT_URL = reverse_lazy('login_redirect')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'var/www/static/')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'var/www/media/')

# needed for pipeline
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'finance/static/'),
)

# always turn on pipeline
PIPELINE = True

# set compressor for css
PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.cssmin.CSSMinCompressor'
PIPELINE_CSSMIN_BINARY = os.path.join(BASE_DIR, 'env/bin/cssmin')

PIPELINE_JS_COMPRESSOR = None

PIPELINE_COMPILERS = (
  'pipeline.compilers.sass.SASSCompiler',
)

PIPELINE_SASS_BINARY = os.path.join(BASE_DIR, 'env/bin/sassc')

# django-pipeline css settings
PIPELINE_CSS = {
    'finance': {
        'source_filenames': (
            'css/bootstrap.min.css',
            'css/main.scss',
        ),
        'output_filename': 'css/finance.css',
        'extra_context': {
            'media': 'screen,projection,handheld',
        },
    },
}

# opbeat settings
OPBEAT = secret.OPBEAT

# recomended settings from `./manage.py check --deploy`
SECURE_BROWSER_XSS_FILTER = True

SECURE_CONTENT_TYPE_NOSNIFF = True

SECRET_KEY = secret.SECRET_KEY

# set up error sending on error
ADMINS = (
    ('admin', 'j.trimailovas@gmail.com'),
)

SERVER_EMAIL = 'finantious@gmail.com'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'finantious@gmail.com'
EMAIL_HOST_PASSWORD = secret.EMAIL_HOST_PASSWORD
EMAIL_PORT = 465
EMAIL_USE_TLS = True
