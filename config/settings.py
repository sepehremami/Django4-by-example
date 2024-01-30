"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from os import path
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/
import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["0.0.0.0", "127.0.0.1"]

SITE_ID = 1

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "taggit",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "blog.apps.BlogConfig",
    "django.contrib.postgres",
    # 'appointment',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [path.join(BASE_DIR / "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"
import time

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
# time.sleep(10)

# from django.db.backends.sq
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "db.sqlite3"
        # 'NAME': os.environ.get('POSTGRES_DB'),
        # 'USER': os.environ.get('POSTGRES_USER'),
        # 'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        # 'HOST': 'db',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

"django-insecure-@bw=2uo_@w)hat8du&3&sy!%bpoa#b0^n))%0n9hp5v&3c@ryf"
# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

STATIC_URL = "static/"


EMAIL_HOST = os.environ.get("EMAIL_HOST")
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
EMAIL_PORT = os.environ.get("EMAIL_PORT")
EMAIL_USE_TLS = os.environ.get("EMAIL_USE_TLS")


LOGGING = {
    "version": 1,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        }
    }, 
    "handlers":{ 
        "loging": { # this name can be anything
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "./logs/debug2.log", # be sure to make dir ./logs
            'formatter': 'verbose',
        }, 
        "blog_handler": { # this name can be anything
            "level": "INFO",
            "class": "logging.StreamHandler",
            'formatter': 'verbose',
        }
    },
     'loggers':{
        'django':{
            "handlers":["loging"],
            "level":"INFO",
            "propagate":True,
        },
        "blog":{
            "handlers":["loging"],
            "level":"INFO",
            "propagate":True,
        }, 
        "blog_debug":
        {
            "handlers":["blog_handler"],
            "level":"DEBUG",
            "propagate":True,
        }, 
        
    },
}

# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,  # Prevent disabling built-in loggers
#     "formatters": {
#         "verbose": {
#             "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
#             "style": "{",
#         }
#     },
#     "handlers": {
#         "logging": {  # Correct handler name
#             "level": "INFO",
#             "class": "logging.FileHandler",
#             "filename": "./logs/debug.log",
#             "formatter": "verbose",
#         },
#     },
#     "loggers": {
#         "django": {  # Configure the Django logger
#             "handlers": ["logging"],
#             "level": "INFO",
#             "propagate": True,
#         },
#         # Add a logger for your app's module
#         "blog": {
#             "handlers": ["logging"],
#             "level": "INFO",
#             "propagate": True,
#         },
#     },
# }
