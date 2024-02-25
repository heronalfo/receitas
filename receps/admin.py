from django.contrib import admin
from .models import Recipes, Categories

@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    ...

@admin.register(Recipes)
class RecipesAdmin(admin.ModelAdmin):
    ...