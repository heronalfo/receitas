from django.urls import path
from .views import *

app_name = "recipes"

urlpatterns = [

  path(
  
      '',
      RecipesListView.as_view(),
      name='recipes'),
      
  path(
  
      'search/',
      RecipesSearchView.as_view(),
      name='search'),
  
  path(
  
      'recipe/<slug:slug>/',
      RecipeView.as_view(),
      name='recipes-recipe'),
  
  path(
  
      'category/<str:name>/',
      CategoryListView.as_view(),
      name='category'),
  
  path(
  
  
      'api/v1/',
      RecipesListViewAPIV1.as_view(),
      name='api-recipes'),
      
  path(
  
  
      'api/v1/detail/',
      RecipesDetailListViewAPIV1.as_view(),
      name='api-detail-recipe'),
                   
]