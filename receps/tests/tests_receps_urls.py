from django.urls import reverse, resolve
from ..models import Categories
from .tests_receps_base import TestsRecepsBase

class RecepsURLsTest(TestsRecepsBase):    
    
    def test_receps_home_url_is_correct(self):
        
        url = reverse('receps:receps')
        self.assertEqual(url, '/receps/')
    
    def test_receps_category_url_is_correct(self):
                
        url = reverse('receps:category', kwargs={'id': 1})        
        self.assertEqual(url, f'/receps/category/1/')
   
    def test_receps_recipe_url_is_correct(self):
        
        url = reverse('receps:receps-recipe', kwargs={'slug': 'test-recipe'})        
        
        self.assertEqual(url, '/receps/recipe/test-recipe/')
        
    def test_receps_search_url_is_correct(self):
        
        url = reverse('receps:search')        
        
        self.assertEqual(url, '/receps/search/')