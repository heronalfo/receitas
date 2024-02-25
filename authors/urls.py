from django.urls import path
from . import views

app_name = "authors"

urlpatterns = [

    path('profile/<str:username>/', views.AuthorsProfile.as_view(), name='profile'),
    
    path('dashboard/', views.AuthorsDashboard.as_view(), name='dashboard'),
    
    path('dashboard/create/', views.AuthorsCreate.as_view(), name='create'),
    
    path('dashboard/<int:id>/edit/', views.AuthorsRecipeEdit.as_view(), name='edit'),
    
    path('dashboard/<int:id>/delete/', views.AuthorsRecipeDelete.as_view(), name='delete'),
    
    


]