from django.urls import path, include
from . import views

app_name = "receps"

urlpatterns = [

  path('', views.receps, name='receps'),
  path('recipe/<slug:slug>/', views.recipe, name='receps-recipe'),
  path('category/<str:name>/', views.category, name='category'),
  
    
]