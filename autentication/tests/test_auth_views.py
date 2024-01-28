from django.test import TestCase
from django.urls import resolve, reverse
from .. import views

class AuthViewsTest(TestCase):

    def test_auth_register_views_is_correct(self):
    
        view = resolve(reverse('auth:register'))
        self.assertEqual(view.func, views.register)
        
    def test_auth_register_views_is_correct(self):
    
        view = resolve(reverse('auth:login'))
        self.assertEqual(view.func, views.login)
        
    def test_auth_register_views_is_correct(self):
    
        view = resolve(reverse('auth:validation'))
        self.assertEqual(view.func, views.validation)
        
    def test_auth_register_views_is_correct(self):
    
        view = resolve(reverse('auth:resend'))
        self.assertEqual(view.func, views.resend)