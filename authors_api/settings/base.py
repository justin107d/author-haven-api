

from pathlib import Path
import environ
import os

env = environ.Env()

ROOT_DIR = Path(__file__).resolve().parent.parent.parent  # need three to get to manage.py level

# points django to where the apps are stored
APPS_DIR = ROOT_DIR / 'core_apps'

BASE_DIR = Path(__file__).resolve().parent.parent


environ.Env.read_env(os.path.join(BASE_DIR / 'settings', '.env')) # this line is trash and did not work


DEBUG = env.bool('DJANGO_DEBUG', False)


DJANGO_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',  #  holding place for domain names and 'verbose' names
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',  # moved to the end for some reason
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'django_filters',
    'django_countries',
    'phonenumber_field',
    'drf_yasg',
    'corsheaders',
]

LOCAL_APPS = [
    'core_apps.common',
    'core_apps.profiles',
    'core_apps.users'
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # added
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware',  # added:  sends broken link notifications to managers
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'authors_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(APPS_DIR / 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',  # added for timezone
                'django.template.context_processors.static',  # added for timezone
                'django.template.context_processors.tz',  # added for timezone
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'authors_api.wsgi.application'


DATABASES = {
    'default': env.db('DATABASE_URL')
}
# DATABASES['default']['ATOMIC_REQUESTS'] = True


PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    # 'django.contrib.auth.hashers.ScryptPasswordHasher',  # removed for some reason
]

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


SITE_ID = 1

ADMIN_URL = 'randomStringThatIsHardToGuess/'

ADMINS = [('''Justin Django''', 'justin107d@gmail.com')]

MANAGERS = ADMINS


STATIC_URL = '/staticfiles/'
STATIC_ROOT = str(ROOT_DIR / 'staticfiles')
STATICFILES_DIR = []
STATICFILES_FINDERS = [  # these are defaults
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]
MEDIA_URL = '/mediafiles/'
MEDIA_ROOT = str(ROOT_DIR / 'mediafiles')

# only allows cors header on /api/
CORS_URLS_REGEX=r'^/api/.*$'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(name)-12s %(asctime)s %(module)s '
            '%(process)d %(thread)d %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        }
    },
    'root': {'level': 'INFO', 'handlers': ['console']},
}