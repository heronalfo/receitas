from django.urls import path, include
from . import views

app_name = "auth" 

urlpatterns = [

    path('register/', views.register, name="register"), 
    path('login/', views.login, name="login"),
    
    path('validation/', views.validation, name='validation'),
    
    path('resend/', views.resend, name='resend'),
    
]