from django.test import TestCase
from django.urls import reverse
from .tests_recipes_base import TestRecipesBase

class RecipesTemplatesTest(TestRecipesBase):

    def test_recipes_home_template_load_is_correct(self):
    
        response = self.client.get(reverse('recipes:recipes'))        
        self.assertTemplateUsed(response, 'pages/recipes.html')
        
    def test_recipes_recipe_template_load_is_correct(self):
    
        response = self.client.get(reverse('recipes:recipes-recipe', kwargs={'slug': 'test-recipe'}))       
        self.assertTemplateUsed(response, 'pages/recipe.html')