from finance.settings import *

DEBUG = False

ALLOWED_HOSTS = ['localhost', '188.166.117.76']

# recomended settings from `./manage.py check --deploy`
SECURE_BROWSER_XSS_FILTER = True

SECURE_CONTENT_TYPE_NOSNIFF = True

SECRET_KEY = secret.SECRET_KEY
