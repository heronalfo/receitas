from django.contrib import admin
from .models import Authors

@admin.register(Authors)
class AuthorsAdmin(admin.ModelAdmin):
   ...