from .common import BASE_DIR

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'demo_exam_26',
        'USER': 'igorsvarc',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}