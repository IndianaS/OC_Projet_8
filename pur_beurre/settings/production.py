from. import *
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration


ALLOWED_HOSTS = ["161.35.123.169", "indiana-p10.pythonclassmates.org", "localhost", "127.0.0.1"]
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pur_beurre',
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

sentry_sdk.init(
    dsn="https://3399934128f24c26bc98e7f74050e73e@o396835.ingest.sentry.io/5250733",
    integrations=[DjangoIntegration()],

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)