import os
from pathlib import Path

#Defines base directory of Project
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

#Key for cryptographic signing
SECRET_KEY = 'django-insecure-=9p0u0(870m0on6#92^plt^eihjw-mhwr0r2@9np9222p7*gqg'

DEBUG = True

#hosts which can access app
ALLOWED_HOSTS = []


#Django's installed apps

INSTALLED_APPS = [
    'django.contrib.admin', #Django's built-in admin panel
    'django.contrib.auth', #Authentication system
    'django.contrib.contenttypes', #Content type manager
    'django.contrib.sessions', #User session hanfler
    'django.contrib.messages', #flash messages
    'django.contrib.staticfiles', #used for CSS,JS and images
    'shop', #shop app in program
    'sslserver',  #Enables HTTPS for development
]

#in charge of request/response processing
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware', #Prevents Cross-Site Request Forgery (CSRF) attacks
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',  #Enables Django’s messaging framework
    'django.middleware.clickjacking.XFrameOptionsMiddleware', #Prevents Clickjacking attacks
]

#main URL config for file
ROOT_URLCONF = 'securecart.urls'

#config for how Django loads and processes HTML templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'shop/templates'],
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

WSGI_APPLICATION = 'securecart.wsgi.application'


#SQLite used as backend for database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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


# Internationalisation settings
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 1800

# Redirect users after login/logout
LOGIN_REDIRECT_URL = '/' # Redirects to homepage after login
LOGOUT_REDIRECT_URL = '/'  # Redirects to homepage after logout
LOGIN_URL = '/accounts/login/'  # Tells Django where the login page is
LOGOUT_URL = '/logout/' #Tells Django where logout page ois

#Define MEDIA settings for serving uploaded images
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

#Enforce HTTPS for security
SECURE_SSL_REDIRECT = False  # Redirects all HTTP traffic to HTTPS
SESSION_COOKIE_SECURE = False  # Ensures session cookies are only sent over HTTPS
CSRF_COOKIE_SECURE = False  # Ensures CSRF cookie is only sent over HTTPS

#Enable HTTP Strict Transport Security (HSTS)
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Applies HSTS to subdomains
SECURE_HSTS_PRELOAD = True  # Allows preloading in browsers for extra security

#For reverse proxies
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

#customer user model
AUTH_USER_MODEL = "shop.Userbalance"