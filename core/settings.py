from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '******'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.apple',
    'allauth.socialaccount.providers.microsoft',
    'allauth.socialaccount.providers.github',
    'blog',
]

LOGIN_REDIRECT_URL = '/'

SITE_ID = 1

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': 'your_client_id',
            'secret': 'your_client_secret',
            'key': ''
        }
    },
    "apple": {
        "APP": {
            # Your service identifier.
            "client_id": "<Your Service ID>",
            # The Key ID (visible in the "View Key Details" page).
            "secret": "<Your Key ID>",
             # Member ID/App ID Prefix -- you can find it below your name
             # at the top right corner of the page, or it’s your App ID
             # Prefix in your App ID.
            "key": "<Your Key>",
            "settings": {
            # The certificate you downloaded when generating the key.
                "certificate_key": """<Your downloaded Key>"""
            },
            "scope": ["email","user"]
        }
    },
    'microsoft': {
        'APP': {
            'client_id': '<Your Application (client) ID>',
            'secret': '<Your Client Secret>',
            'key': '',  # Not typically needed for Microsoft OAuth2
        },
        'scope': ['User.Read']  # Adjust scopes as per your requirements
    },
    'github': {
        'APP': {
            'client_id': '<Your Client ID>',
            'secret': '<Your Client Secret>',
            'key': '',  # Not typically needed for GitHub OAuth2
        },
        'scope': ['read:user', 'user:email']  # Adjust scopes as per your requirements
    }
}

SOCIALACCOUNT_AUTO_SIGNUP = True
SOCIALACCOUNT_LOGIN_ON_GET = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'core.urls'

import os
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # Required for admin navigation sidebar
                'django.contrib.auth.context_processors.auth',  # Required for admin and authentication
                'django.contrib.messages.context_processors.messages',  # Required for admin messages
            ],
        },
    },
]

ACCOUNT_LOGIN_TEMPLATE = 'blog/login.html'
ACCOUNT_SIGNUP_TEMPLATE = 'blog/signup.html'
ACCOUNT_LOGOUT_TEMPLATE = 'blog/logout.html'

REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'your_project.serializers.CustomRegisterSerializer',
}

AUTHENTICATION_BACKENDS = [
    
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
    
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ACCOUNT_EMAIL_VERIFICATION = 'none'
