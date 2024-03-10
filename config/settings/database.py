from .base_dir import BASE_DIR

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        
        'NAME': BASE_DIR / 'sqlite3.db',
#        
#        'USER': os.environ.get("DATABASE_USER"),
#        
#        'PASSWORD': os.environ.get("DATABASE_PASSWORD"),
#        
#        'HOST': os.environ.get("DATABASE_HOST"),
#        
#        'PORT': os.environ.get("DATABASE_PORT"),
    }
}