from finance.settings import *

DEBUG = True

ALLOWED_HOSTS = []

# do not send statistics to opbeat when testing
MIDDLEWARE_CLASSES = tuple(
    middleware for middleware in MIDDLEWARE_CLASSES
    if middleware != "opbeat.contrib.django.middleware.OpbeatAPMMiddleware"
)
