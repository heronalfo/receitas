from django.urls import path, include
from . import views

urlpatterns = [

    path('cadastro/', views.cadastro, name="cadastro"), 
    path('login/', views.logar, name="login"),
    
    path('validacao/', views.validacao, name='validacao'),
    
    path('reenviar_codigo/', views.reenviar, name='reenviar_codigo')
    
]