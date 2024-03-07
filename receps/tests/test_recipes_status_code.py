from django.urls import reverse, resolve
from .tests_recipes_base import TestRecipesBase
from time import sleep
import pdb

class RecipesStatusCodeTest(TestRecipesBase):

    def test_recipes_home_status_code_is_200(self):
        
        response = self.client.get(reverse('recipes:recipes'))
                       
        self.assertEqual(response.status_code,  200)
                        
    def test_recipes_recipe_status_code_is_200(self):
      
        response = self.client.get(reverse('recipes:recipes-recipe', kwargs={'slug': 'test-recipe'}))              
        self.assertEqual(response.status_code,  200)
        
    def test_recipes_search_status_code_is_200(self):
      
        response = self.client.get(reverse('recipes:search'))              
        self.assertEqual(response.status_code, 302)