#encoding:utf-8
# Django settings for ct2 project.
# Dependencias
# south
# python-social-auth

DEBUG = True
TEMPLATE_DEBUG = DEBUG

import os
RUTA_PROYECTO = os.path.dirname(os.path.realpath(__file__))



ADMINS = (
    ('Saul Enrrique Pineda Torres', 'enrique_wx@hotmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'db_clicktotal',                      # Or path to database file if using sqlite3.
        'USER': 'viewor',                      # Not used with sqlite3.
        'PASSWORD': 'viewor_12',                  # Not used with sqlite3.
        'HOST': '198.199.120.36',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
    }
}


# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Mexico_City'
# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'es-Mx'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(RUTA_PROYECTO,'../public/upload')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/public/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/static/admin/'
# Additional locations of static files
STATICFILES_DIRS = (
     os.path.join(RUTA_PROYECTO,'../public/static/'),
)


# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'l&xm@7=j7+okpp-oqn)-m81ag)6yo*@_qu(2f1*zz@ld_%+%b7'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'social_auth.middleware.SocialAuthExceptionMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'configuracion.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'configuracion.wsgi.application'

TEMPLATE_DIRS = (
     os.path.join(RUTA_PROYECTO,'../public/templates/'),
)

#perfil del usuario 
AUTH_PROFILE_MODULE = 'apps.usuarios.models.perfil.Perfil'


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'social.apps.django_app.default',
    'south',
    'imagekit',
    'apps.usuarios',
    'apps.empresas',
    'apps.promociones',
    'apps.cupones',
    'apps.comentarios',
    'apps.pagos',

    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}



TEMPLATE_CONTEXT_PROCESSORS = ("django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "social.apps.django_app.context_processors.backends",
    "social.apps.django_app.context_processors.login_redirect",
    "django.contrib.messages.context_processors.messages"
)



AUTHENTICATION_BACKENDS = (
    'social.backends.twitter.TwitterOAuth',
    'social.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

#Twitter
SOCIAL_AUTH_TWITTER_KEY = 'BRdqcpPEe5C9NZZ7ZEZ05Q'
SOCIAL_AUTH_TWITTER_SECRET = 'eGrPixqmidtZpLCzNdUB96zVht8xrRLoiNLnJ2aZsbQ'
# Facebook
SOCIAL_AUTH_FACEBOOK_KEY = '188980267933208'
SOCIAL_AUTH_FACEBOOK_SECRET = '5bc9b759bf791f7eb213e49d2d4ab28d'

""" ***  key(consola) para la api de Google Places *** """
API_KEY_GOOGLE_PLACES        = 'AIzaSyCy1NFjXXz9R2VV9vaZ0VQVKolvKyazR8k'

# Las siguietes 3 lineas sirven para configurar el despues del login, la url de login, y el error
FACEBOOK_SOCIAL_AUTH_RAISE_EXCEPTIONS = True
SOCIAL_AUTH_RAISE_EXCEPTIONS = True
RAISE_EXCEPTIONS = True
DEBUG = True

# rutas python-social-auth
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_LOGIN_ERROR_URL = '/'
SOCIAL_AUTH_LOGIN_URL = '/'
# Este campo permite redirigir a los nuevos usuarios -- SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/new-users-redirect-url/'
SOCIAL_AUTH_DISCONNECT_REDIRECT_URL = '/'

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email',
    'user_about_me',
    'user_status',
    'user_relationship_details',
    'user_location',
    'publish_actions',
    'user_likes',
    'user_location',
    'user_subscriptions',
    'publish_stream',
    'read_stream',
    'read_friendlists',
    'user_interests',
    'user_website',
    'user_birthday',
    'user_hometown',
    'user_checkins',
    'user_relationships',
    'user_religion_politics',
]
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {'locale': 'es_LA'}
SOCIAL_AUTH_FACEBOOK_EXTRA_DATA = [
    ('id', 'id'),
    ('about', 'about'),
    ('address', 'address'),
    ('bio', 'bio'),
    ('birthday', 'birthday'),
    ('devices', 'devices'),
    ('email', 'email'),
    ('favorite_athletes', 'favorite_athletes'),
    ('favorite_teams', 'favorite_teams'),
    ('first_name', 'first_name'),
    ('last_name', 'last_name'),
    ('gender', 'gender'),
    ('hometown', 'hometown'),
    ('inspirational_people', 'inspirational_people'),
    ('interested_in', 'interested_in'),
    ('languages', 'languages'),
    ('political', 'political'),
    ('relationship_status', 'relationship_status'),
    ('location', 'location'),
    ('work', 'work'),
    ('movies', 'movies'),
    ('music', 'music'),
    ('interests', 'interests'),
    ('checkins', 'checkins')
]

SOCIAL_AUTH_TWITTER_EXTRA_DATA = [('profile_image_url', 'profile_image_url'),('screen_name', 'screen_name')]


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'filperempresa@gmail.com'
EMAIL_HOST_PASSWORD = 'filper1234'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
