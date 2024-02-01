from django.test import TestCase
from django.urls import reverse

class AuthTemplatesTest(TestCase):

    def test_auth_register_template_load_is_correct(self):
    
        response = self.client.get(reverse('auth:register'))        
        self.assertTemplateUsed(response, 'pages/register.html')
        
    def test_auth_login_template_load_is_correct(self):
    
        response = self.client.get(reverse('auth:login'))       
        self.assertTemplateUsed(response, 'pages/login.html')       
