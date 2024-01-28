from django.test import TestCase
from django.urls import reverse

class AuthStatusCodeTest(TestCase):

    def test_auth_register_status_code_is_200(self):
    
        response = self.client.get(reverse('auth:register'))
        self.assertEqual(response.status_code, 200)
    
    def test_auth_login_status_code_is_200(self):
    
        response = self.client.get(reverse('auth:login'))
        self.assertEqual(response.status_code,  200)
        
    def test_auth_validation_status_code_is_302(self):
    
        response = self.client.get(reverse('auth:validation'))        
        self.assertEqual(response.status_code, 302)
    
    def test_auth_resend_status_code_is_302(self):
    
        response = self.client.get(reverse('auth:resend'))
        self.assertEqual(response.status_code, 302)