from django.urls import reverse, resolve
from .tests_receps_base import TestsRecepsBase
import pdb

class RecepsStatusCodeTest(TestsRecepsBase):

    def test_receps_home_status_code_is_200(self):
        
        response = self.client.get(reverse('receps:receps'))
        
        pdb.set_trace()
                       
        self.assertEqual(response.status_code,  200)
            
    def test_receps_category_status_code_is_200(self):
        
        response = self.client.get(reverse('receps:category', kwargs={'name': 'BreakFast'}))
        self.assertEqual(response.status_code,  200)
        
    def test_receps_recipe_status_code_is_200(self):
      
        response = self.client.get(reverse('receps:receps-recipe', kwargs={'slug': 'test-recipe'}))              
        self.assertEqual(response.status_code,  200)