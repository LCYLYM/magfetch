
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third Party Apps
    'widget_tweaks',
    'django_cleanup',
    'django_cool_paginator',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    # 'corsheaders',
    # 'rest_framework',
    # Local Apps
    'accounts',
    'system_data',
    'suspicious',
    'utils',
    'contribution',
]

SITE_ID = 1

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    # 'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # CorsHeader Middleware before CommonMiddleware
    # 'corsheaders.middleware.CorsMiddleware',
    # CorsHeader Middleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'magfetch.urls'

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
            # 'loaders': [
            #     ('django.template.loaders.cached.Loader', [
            #         'django.template.loaders.filesystem.Loader',
            #         'django.template.loaders.app_directories.Loader',

            #     ]),
            # ],
        },
    },
]

WSGI_APPLICATION = 'magfetch.wsgi.application'


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
LANGUAGE_CODE   = 'en-us'
TIME_ZONE       = 'Asia/Dhaka'
USE_I18N        = True
USE_L10N        = True
USE_TZ          = False

# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'
# USE_I18N = True
# USE_L10N = True
# USE_TZ = True

# Allauth
LOGIN_URL = '/account/login/'
LOGOUT_URL = '/'
LOGIN_REDIRECT_URL = '/'
SITE_NAME = 'magFetch'
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 7
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300
ACCOUNT_USERNAME_MIN_LENGTH = 1
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_SIGNUP_PASSWORD_VERIFICATION = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = '/'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_EMAIL_SUBJECT_PREFIX = 'magFetch'
ACCOUNT_USERNAME_BLACKLIST =['robot', 'hacker', 'virus', 'spam']
ACCOUNT_ADAPTER = 'magfetch.adapter.UsernameMaxAdapter'


# Cool Paginator
COOL_PAGINATOR_NEXT_NAME        = "next"
COOL_PAGINATOR_PREVIOUS_NAME    = "previous"
COOL_PAGINATOR_SIZE             = "SMALL"
COOL_PAGINATOR_ELASTIC          = "300px"

# File Validation Staffs
ALLOWED_FILE_TYPES = ['.doc', '.docx', '.jpg', '.jpeg', '.png',
                 '.svg', '.DOC', '.DOCX', '.JPG', '.JPEG', '.PNG', '.SVG']
FILE_TYPES = ['.doc', '.docx', '.jpg', '.jpeg', '.png', '.svg']

IMAGE_TYPES = ['.jpg', '.jpeg', '.png', '.svg']
DOCUMENT_TYPES = ['.doc', '.docx']

# 1.5MB - 1621440
# 2.5MB - 2621440
# 5MB - 5242880
# 10MB - 10485760
# 20MB - 20971520
# 50MB - 5242880
# 100MB 104857600
# 250MB - 214958080
# 500MB - 429916160
MAX_UPLOAD_SIZE = 2621440


# # Static Files
# STATIC_URL = '/static/'
# MEDIA_URL = '/media/'

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static_proj'),
# ]
# STATIC_ROOT = os.path.join('static_cdn', 'static_root')
# MEDIA_ROOT = os.path.join('static_cdn', 'media_root')

# STATICFILES_FINDERS = [
#     'django.contrib.staticfiles.finders.FileSystemFinder',
#     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
# ]


# Neededf for CorsHeader (accept connections from everywhere)
# CORS_ORIGIN_ALLOW_ALL = True

# CORS_ALLOW_HEADERS = (
#     'x-requested-with',
#     'content-type',
#     'accept',
#     'origin',
#     'authorization',
#     'x-csrftoken',
#     'token',
#     'x-device-id',
#     'x-device-type',
#     'x-push-id',
#     'dataserviceversion',
#     'maxdataserviceversion'
# )
# CORS_ALLOW_METHODS = (
#     'GET',
#     'POST',
#     'PUT',
#     'PATCH',
#     'DELETE',
#     'OPTIONS'
# )
