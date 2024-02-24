from django.urls import path, include
from . import views

app_name = "receps"

urlpatterns = [

  path('', views.RecepsListView.as_view(), name='receps'),
  path('search/', views.SearchView.as_view(), name='search'),
  path('recipe/<slug:slug>/', views.RecepeView.as_view(), name='receps-recipe'),
  
  path('category/<str:name>/', views.CategoryListView.as_view(), name='category'),
  
    
]