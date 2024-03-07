from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('autentication.urls')),
    path('recipes/', include('receps.urls')),
    path('authors/', include('authors.urls')),
]
