import os
from pathlib import Path
import netifaces
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-t(7-hv3y)0zp^i)q(40kc^06zd8_%x2d)@og*mf0k!=c6d&$x!'
DEBUG = True

def get_ipaddress():
    adr = ['https://hpg.wega.ponics.ru', 'http://hpg.wega.ponics.ru', ]
    for interface in netifaces.interfaces():
        if netifaces.ifaddresses(interface):
            # print('netifaces.ifaddresses(interface)', netifaces.ifaddresses(interface))
            if netifaces.AF_INET in netifaces.ifaddresses(interface):
                for link in netifaces.ifaddresses(interface)[netifaces.AF_INET]:
                    adr.append(f"http://{link[ 'addr']}")
                    adr.append(f"https://{link['addr']}")
            
    return adr

ALLOWED_HOSTS=["*"]
CSRF_TRUSTED_ORIGINS=get_ipaddress()

LOGIN_URL = '/auth/login/'

INSTALLED_APPS = [
        'wagtail.contrib.forms',
        'wagtail.contrib.redirects',
        'wagtail.embeds',
        'wagtail.sites',
        'wagtail.users',
        'wagtail.snippets',
        'wagtail.documents',
        'wagtail.images',
        'wagtail.search',
        'wagtail.admin',
        'wagtail',
        
        'modelcluster',
        'taggit',
        
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.telegram',
    
    
    'django_tables2',
    'compressor',
    'import_export',
    'fancybox',
    'django_cleanup.apps.CleanupConfig',
    
    'wega_auth',
    'calc',
    'home',
    'wiki',
    'mixer',
]

MIDDLEWARE = [
    # 'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'project.middleware.Wega',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'project.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        'test': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'test_db.sqlite3',
        },
    },
 
    
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
COMPRESS_ROOT = STATIC_ROOT
MEDIA_URL = '/media/'
PROJECT_DIR  = Path(__file__).resolve().parent
STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
]

AUTHENTICATION_BACKENDS =  ("allauth.account.auth_backends.AuthenticationBackend","project.backend.EmailBackend")

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',

    'compressor.finders.CompressorFinder',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '[%(asctime)s] %(levelname)s: %(message)s',
            'datefmt': '%d/%m/%Y %H:%M:%S',
        },
        
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {lineno} {message}',
            'style': '{',
        },
        
    },
    'handlers': {
        
        'mail_admins': {
            'class': 'django.utils.log.AdminEmailHandler',
            'level': 'INFO',
            # But the emails are plain text by default - HTML is nicer
            'include_html': True,
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        #     # Log to a text file that can be rotated by logrotate
        'logfile': {
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': 'server.log',
            'level': 'INFO',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', ],
            'level': 'ERROR',
            'propagate': True,
        },
        'django': {
            'handlers': ['logfile', 'console', ],
            'level': 'ERROR',
            'propagate': False,
        },
        
    },
}
LANGUAGE_CODE = 'ru'
LANGUAGES = ( ( 'en', "English", ), ( 'ru', "Russian", ), )
HOSTNAME='/'
SHORT_DATETIME_FORMAT="%Y-%m-%d"
# CACHES={'default':{'BACKEND': 'django.core.cache.backends.dummy.DummyCache',}}
MIDDLEWARE+=['wagtail.contrib.redirects.middleware.RedirectMiddleware',]
WAGTAIL_SITE_NAME = 'calc'
SITE_ID = 1
ACCOUNT_SIGNUP_REDIRECT_URL = "/"
LOGIN_REDIRECT_URL = "/"
SOCIAL_LOGIN_REDIRECT_URL = "/"

from .default_user import *