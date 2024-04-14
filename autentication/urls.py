from django.urls import path, include
from . import views

app_name = "auth" 

urlpatterns = [

    path('register/', views.AuthRegister.as_view(), name="register"),
     
    path('login/', views.AuthLogin.as_view(), name="login"),
    
    path('validation/', views.AuthValidation.as_view(), name='validation'),
    
    path('resend/', views.AuthResend.as_view(), name='resend'),
    
    path('logout/', views.AuthLogout, name='logout'),
    
]