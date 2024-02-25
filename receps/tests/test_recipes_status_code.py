from django.urls import reverse, resolve
from .tests_receps_base import TestsRecepsBase
from time import sleep
import pdb

class RecepsStatusCodeTest(TestsRecepsBase):

    def test_receps_home_status_code_is_200(self):
        
        response = self.client.get(reverse('receps:receps'))
                       
        self.assertEqual(response.status_code,  200)
                        
    def test_receps_recipe_status_code_is_200(self):
      
        response = self.client.get(reverse('receps:receps-recipe', kwargs={'slug': 'test-recipe'}))              
        self.assertEqual(response.status_code,  200)
        
    def test_receps_search_status_code_is_200(self):
      
        response = self.client.get(reverse('receps:search'))              
        self.assertEqual(response.status_code, 302)