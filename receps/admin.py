from django.contrib import admin
from .models import Receps, Categories

@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    ...

@admin.register(Receps)
class RecepsAdmin(admin.ModelAdmin):
    ...