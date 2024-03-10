from . import BASE_DIR

STATIC_URL = 'static/'

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = [

  BASE_DIR / 'statics',


]