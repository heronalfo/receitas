from django.test import TestCase
from django.urls import reverse

class AuthURLsTest(TestCase):

    def test_auth_url_register(self):
    
        url =  reverse('auth:register')       
        self.assertEqual(url, '/auth/register/')
        
    def test_auth_url_login(self):
    
        url = reverse('auth:login')
        self.assertEqual(url, '/auth/login/')
    
    def test_auth_url_resend(self):
    
        url = reverse('auth:resend')
        self.assertEqual(url, '/auth/resend/')
    
    def test_auth_url_validation(self):
    
        url = reverse('auth:validation')
        self.assertEqual(url, '/auth/validation/')