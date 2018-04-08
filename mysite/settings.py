"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

import django.contrib.auth

# import pymysql
# pymysql.install_as_MySQLdb()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6dauc_#35$502m5ms4wod_7ts!rcn52w7=d%amv_i9!p)&a!dv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['13.124.243.206','localhost','127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',

    'django.contrib.staticfiles',

    'widget_tweaks',

    # 'startpolls',
    'realestate',
    'post_service',
    'user_manager',
    # 'rest_framework',
    # 'rest_framework_swagger',
]


LOGIN_EXEMPT_URLS=[
    'admin',
    'realestate/register',
    'realestate/template_typography',
    'realestate/template_index',
    'realestate/template_tables',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'realestate.middleware.LoginRequiredMiddleware',
]




ROOT_URLCONF = 'mysite.urls'

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
            # 'init_command': 'SET innodb_strict_mode=1',
            # 'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
            # 'init_command':"SET sql_mode='STRICT_TRANS_TABLES', innodb_strict_mode=1",
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {

        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.mysql',
        #http://54.224.103.57/phpmyadmin/
        #http://13.124.243.206/phpmyadmin/
        #'NAME': 'kunta',
        # 'NAME': 'kunta_2',
        'NAME': 'kunta_3',
        'USER': 'root',
        'PASSWORD': 'dlwjdgns',
        # 'HOST': '54.224.103.57',
        # 'HOST': '13.124.243.206',
        # 'HOST': '13.125.53.78',
        'HOST': '13.124.209.5',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES', innodb_strict_mode=1",
            'charset': 'utf8',
            'use_unicode': True,
        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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

#LOGIN_URL = '/user/login/'
#LOGIN_REDIRECT_URL = '/board/'

LOGIN_URL = '/realestate/login/'
# LOGIN info root dlwjdgns8524!
# LOGIN_REDIRECT_URL = '/realestate/main/'    #after login, when we use login function provided by django auth
LOGIN_REDIRECT_URL = '/realestate/search/'    #after login, when we use login function provided by django auth


SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # default False

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

# DATABASE_OPTIONS = {'charset': 'utf8'}
TIME_ZONE = 'Asia/Seoul'
LANGUAGE_CODE = 'ko-kr'

# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'
# TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
