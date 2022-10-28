from .base import *
from .base import env

DEBUG = True

SECRET_KEY = env(
    'DJANGO_SECRET_KEY',
    default='django-insecure-bnw$7^@btnzaz+%=35va-=bv3gosvkroq2tpy@ct!xe_q_3qfw'
)

ALLOWED_HOSTS = ['localhost', '0.0.0.0', '127.0.0.1']

