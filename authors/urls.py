from django.urls import path
from . import views

app_name = "authors"

urlpatterns = [

    path('profile/<str:username>/', views.profile, name='profile'),
    
    path('dashboard/', views.dashboard, name='dashboard'),
    
    path('dashboard/create/', views.create, name='create'),
    
    path('dashboard/<int:id>/edit/', views.edit, name='edit'),
    
    path('dashboard/<int:id>/delete/', views.delete, name='delete'),
    
    


]