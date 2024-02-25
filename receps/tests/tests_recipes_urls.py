from django.urls import reverse, resolve
from ..models import Categories
from .tests_recipes_base import TestsRecipesBase

class RecipesURLsTest(TestsRecipesBase):    
    
    def test_recipes_home_url_is_correct(self):
        
        url = reverse('recipes:recipes')
        self.assertEqual(url, '/recipes/')
    
    def test_recipes_category_url_is_correct(self):
                
        url = reverse('recipes:category', kwargs={'name': 'Teste'})        
        self.assertEqual(url, f'/recipes/category/Teste/')
   
    def test_recipes_recipe_url_is_correct(self):
        
        url = reverse('recipes:recipes-recipe', kwargs={'slug': 'test-recipe'})        
        
        self.assertEqual(url, '/recipes/recipe/test-recipe/')
        
    def test_recipes_search_url_is_correct(self):
        
        url = reverse('recipes:search')        
        
        self.assertEqual(url, '/recipes/search/')