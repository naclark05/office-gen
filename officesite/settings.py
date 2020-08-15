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

    import django_heroku # for heroku dev

    from dotenv import load_dotenv # environment variables for secrets
    load_dotenv() # loads env vars

    import os
    from django.core.exceptions import ImproperlyConfigured


    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


    MIDDLEWARE_CLASSES = (
    # Simplified static file serving.
    # https://warehouse.python.org/project/whitenoise/
    'whitenoise.middleware.WhiteNoiseMiddleware', 
    )

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
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') #dev: ''
    STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    ) #dev: ['/Users/nikclarks/djproj/officesite/offgen/static/']
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage' #heroku 
    COMPRESS_ENABLED = os.environ.get('COMPRESS_ENABLED', False)

    import dj_database_url # heroku

    DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)
    django_heroku.settings(locals()) # activate django-heroku

# dev settings
class Dev(Base):
    DEBUG = True
    SECRET_KEY = values.Value("SECRET_KEY")

# deploy settings
class Prod(Base):
    # read errors while debug is false for heroku
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': ('%(asctime)s [%(process)d] [%(levelname)s] ' +
                           'pathname=%(pathname)s lineno=%(lineno)s ' +
                           'funcname=%(funcName)s %(message)s'),
                'datefmt': '%Y-%m-%d %H:%M:%S'
            },
            'simple': {
                'format': '%(levelname)s %(message)s'
            }
        },
        'handlers': {
            'null': {
                'level': 'DEBUG',
                'class': 'logging.NullHandler',
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose'
            }
        },
        'loggers': {
            'testlogger': {
                'handlers': ['console'],
                'level': 'INFO',
            }
        }
    }
    DEBUG_PROPAGATE_EXCEPTIONS = True # heroku prod
    DEBUG = False # heroku prod


    


    




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







