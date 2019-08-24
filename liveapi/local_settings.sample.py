# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
import os

SECRET_KEY = '_0$5cs*7)c_&vhwhcqo+dimoz%1lv5!w0kn_ct=$(ao1ltdyae'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'db.sqlite3'),
    }
}

CACHES = {
    "default": {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

BITCOIN_USER = 'bitcoin'
BITCOIN_PASSWORD = 'password'
BITCOIN_HOST = '172.17.0.1'
BITCOIN_PORT = '8332'

KAFKA_BOOTSTRAP_SERVICE = ''
KAFKA_GROUP_ID = ''

BTC_KEYSPACE = 'bitcoin'
CASSANDRA_HOST = '172.17.0.1'
CASSANDRA_PORT = '9042'