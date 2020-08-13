"""
Django settings for officesite project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""


from configurations import Configuration, values

# base settings
class Base(Configuration):

    from dotenv import load_dotenv # environment variables for secrets
    load_dotenv() # loads env vars

    

    import os
    from django.core.exceptions import ImproperlyConfigured

    import dj_database_url

    DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv("DB_NAME"),
        'USER': 'nikki',
        'PASSWORD': os.getenv("DB_PASSWORD"),
        'HOST': 'localhost',
        'PORT': '',
        }
    }


    ALLOWED_HOSTS = []

    INSTALLED_APPS = [
    'offgen',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    ]

    MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    ROOT_URLCONF = 'officesite.urls'

    TEMPLATES = [
        {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['offgen/templates/offgen'],
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

    WSGI_APPLICATION = 'officesite.wsgi.application'

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

    

    STATIC_URL = '/static/'
    STATIC_ROOT = ''
    STATICFILES_DIRS = ['/Users/nikclarks/djproj/officesite/offgen/static/']



# dev settings
class Dev(Base):
    DEBUG = True
    SECRET_KEY = values.Value("SECRET_KEY")

# deploy settings
class Prod(Base):

    import django_heroku # for heroku dev
    
    django_heroku.settings(locals()) # activate django-heroku

    DEBUG = False


    




# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/



# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases


# SECURITY WARNING: don't run with debug turned on in production!




# Application definition





# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators




# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/







