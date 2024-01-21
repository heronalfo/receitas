from django.urls import path, include
from . import views

urlpatterns = [

  path('', views.receps, name='receps'),
  path('recipe/<int:id>/', views.recipe, name='receps-recipe'),
  path('category/<int:id>/', views.category, name='category'),
  
    
]