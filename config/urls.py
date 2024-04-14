from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404

handler404 = 'receps.views.recipes_handler404.recipes_handler404'

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('autentication.urls')),
    path('recipes/', include('receps.urls')),
    path('authors/', include('authors.urls')),
]
