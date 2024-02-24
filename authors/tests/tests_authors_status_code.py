from django.urls import reverse, resolve
from .tests_authors_base import TestsAuthorsBase
from time import sleep
import pdb

class AuthorsStatusCodeTest(TestsAuthorsBase):

    def test_authors_profile_status_code_is_200(self):
        
        response = self.client.get(reverse('authors:profile', args=('usertest', )))
                               
        self.assertEqual(response.status_code, 200)
        
    def test_authors_dashboard_status_code_is_302(self):
        
        response = self.client.get(reverse('authors:dashboard'))
                               
        self.assertEqual(response.status_code, 302)
        
    def test_authors_edit_status_code_is_302(self):
        
        response = self.client.get(reverse('authors:edit', args=(1, )))
                               
        self.assertEqual(response.status_code, 302)
    
    def test_authors_create_status_code_is_302(self):
        
        response = self.client.get(reverse('authors:create'))
                               
        self.assertEqual(response.status_code, 302)