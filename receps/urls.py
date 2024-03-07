from django.urls import path, include
from . import views

app_name = "recipes"

urlpatterns = [

  path(
  
      '',
      views.RecipesListView.as_view(),
      name='recipes'),
      
  path(
  
      'search/',
      views.RecipesSearchView.as_view(),
      name='search'),
  
  path(
  
      'recipe/<slug:slug>/',
      views.RecipeView.as_view(),
      name='recipes-recipe'),
  
  path(
  
      'category/<str:name>/',
      views.CategoryListView.as_view(),
      name='category'),
      
  path(
  
      'api/v1/',
      views.RecipesListViewAPIV1.as_view(),
      name='recipes-api-v1'),
  
  path(
  
      'api/v1/<slug:slug>/',
      views.RecipeViewAPIV1.as_view(),
      name='recipe-api-v1'),
  
]