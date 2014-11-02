"""
Django settings for mvp_landing project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os


# gets the file where were at of the directory name of that file, which is "src"
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# this is a reference:
# BASE_DIR = '/home/dee-mann/Desktop/skillshare/src'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'faiik0n61x)+=8m&z-o())ifijj(mii31+28_1xg_cb%td1*%3'

# SECURITY WARNING: don't run with debug turned on in production!
# for when we want to find errors.
DEBUG = True

TEMPLATE_DEBUG = DEBUG
#TEMPLATE_DEBUG = True

# EXAMPLE:
# when...
#
#DEBUG = False
#TEMPLATE_DEBUG = False
#
# enable...
#
# this ensures security only on specific domains
# ALLOWED_HOSTS = ['www.yourwebsite.com']

ALLOWED_HOSTS = []

# provide our get_profile()
# provides authentication to the Django backend
AUTH_PROFILE_MODULE = 'drinker.Drinker'

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    
    # User authentication in Django
    # The permission model in django.contrib.auth depends on django.contrib.contenttypes.
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'signups',
    'drinker',
    'dragdrop',
)

# Goes through MIDDLEWARE_CLASSES first then looks for "views" and looks for INSTALLED_APPS
MIDDLEWARE_CLASSES = (
    # for authentication in web requests
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    # for authentication in web requests
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# where URL's are handles in each part 
ROOT_URLCONF = 'mvp_landing.urls'

WSGI_APPLICATION = 'mvp_landing.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        # sqlite3 automatically generates tables using these two statements
        # not reccommended for live deployment
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        #'USER':'',
        #'PASSWORD':'', 
        #'HOST':'',
        #'PORT':'',
            
        # were using MySQL instead
        #'ENGINE': 'django.db.backends.mysql',
        #'NAME': 'mvp_landing_db',
        #'USER': 'mvpland',
        #'PASSWORD': '1293819318930JDSIOAJD!@#$*',
        #'HOST': 'mysql.server',   # Or an IP Address that your DB is hosted on
        #'PORT': '3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

# what is rendered by the browser, not so much Django
STATIC_URL = '/static/'

# setting our template location
# note this is a tuple
TEMPLATE_DIRS = (
    
    # this joins the path of the folder that is 1 up the base directory
    # it will look for static and under static it will look for templates 
    os.path.join(os.path.dirname(BASE_DIR), "static", "templates"),
    
    # this is a reference:
    # '/home/dee-mann/Desktop/skillshare/static/templates/',

)



if DEBUG:
    MEDIA_URL = '/media/'
    STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "static-only")
    
    # where pictures are stored
    MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "media")
    
    # a tuple that collects CSS and JavaScript files
    # useful for production and collecting static files.
    # note that this is a tuple.
    STATICFILES_DIRS = (
        os.path.join(os.path.dirname(BASE_DIR), 'static', 'static'),
    )