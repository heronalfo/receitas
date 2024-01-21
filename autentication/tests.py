from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class TestesAuth(TestCase):

    def TesteCadastro(self):
    
        dados = {        
        'email': 'autis@gmail.com',
        'senha': 'Br3+-bahia',
        'senha2': 'Br3+-bahia'
        
        }
        
        resposta = self.client.post(reverse('autenticacao:cadastrar'), dados=dados)
        
        print(resposta)