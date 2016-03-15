"""
Django settings for vybor_project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
import os
import socket


if True:
    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    #ROOT_PATH = os.path.dirname(__file__)
    PROJECT_ROOT = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
                os.path.join(PROJECT_ROOT, 'templates'),
            ],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.contrib.auth.context_processors.auth',
                    'django.template.context_processors.debug',
                    'django.template.context_processors.i18n',
                    'django.template.context_processors.media',
                    'django.template.context_processors.static',
                    'django.template.context_processors.tz',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]


    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = '2@jtmvj088#$(j29x5z7n(#e7b**d-gjp6c4rz$+5w3y1br@cs'

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = False

    ALLOWED_HOSTS = ['tibi-et-igni.myjino.ru',]


    # Application definition

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'home',
        'contacts',
        'projects',
        'documents',
        'news',
        'advisors',
        'strategy',
        'partners',
        'video',
        'images',
    )

    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

    ROOT_URLCONF = 'vybor_project.urls'

    WSGI_APPLICATION = 'vybor_project.wsgi.application'


    # Database
    # https://docs.djangoproject.com/en/1.7/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

    # Internationalization
    # https://docs.djangoproject.com/en/1.7/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'Europe/Moscow'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True


    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.7/howto/static-files/

    STATIC_URL = '/static/'
    MEDIA_URL = '/media/'


    STATIC_ROOT = os.path.join(os.path.expanduser('~'), 'domains/tibi-et-igni.myjino.ru/static')
    #STATICFILES_DIRS = [
    #    os.path.join(PROJECT_ROOT, "static"),
    #]
    MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media/')
else:
    DEBUG = True
