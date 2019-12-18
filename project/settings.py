import os
from dotenv import load_dotenv
load_dotenv()


from environs import Env

env = Env()
env.read_env()

DEBUG = env.bool("DEBUG")

DATABASES = {}

DATABASES['default'] = eval(os.getenv("DATABASES"))

SECRET_KEY = os.getenv("SECRET_KEY")

INSTALLED_APPS = ['datacenter']

ROOT_URLCONF = "project.urls"

ALLOWED_HOSTS = ['*']


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]

USE_L10N = True

LANGUAGE_CODE = 'ru-ru'