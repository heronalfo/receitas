from django.urls import path
from . import views

app_name = "authors"

urlpatterns = [

    path('profile/<str:username>/', views.profile, name='profile')


]