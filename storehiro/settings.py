
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#Crea una ruta dentro del proyecto de la siguiente manera
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l4mt21-zzijj#_96w!)p+e8b6jxaq5_g=hi4ek1arcawj%+4v%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#Si lo dejamos en true cuando se implemente en produccion veremos 
#de si en caso falla la pagina el error de forma detallada.


ALLOWED_HOSTS = []


# Application definition
#Lista que indica todas las aplicaciones que estan habilitadas en
#DJANGO
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'products',
    'categories',
    'users',
    'carts',

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

#
ROOT_URLCONF = 'storehiro.urls'

#Con esto le indicamos a django que no solo vamos a usar el modelo
#AUTH_USER_MODEL= 'users.User'


#Una lista que contiene todos los motores de plantillas que se utilizara con DJANGO.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'], #Esto es para que pueda reconocer la carpeta templates
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

WSGI_APPLICATION = 'storehiro.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
#URL usada cuando se hace referencia a archivos estaticos.
STATIC_URL = '/static/'

#Aqui va estar direcciones donde estan los 
#archivos estaticos
STATICFILES_DIRS=[(
    os.path.join(BASE_DIR,'static')
)]



#Vamos a generar un par de constantes...
#
MEDIA_URL = '/media/'

#Ruta absoluta del sistema de archivos que contendra los archivos subidos por el usuario
MEDIA_ROOT =  os.path.join(BASE_DIR,'media')



