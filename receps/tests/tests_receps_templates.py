from django.test import TestCase
from django.urls import reverse
from .tests_receps_base import TestsRecepsBase

class RecepsTemplatesTest(TestsRecepsBase):

    def test_receps_home_template_load_is_correct(self):
    
        response = self.client.get(reverse('receps:receps'))        
        self.assertTemplateUsed(response, 'pages/receps.html')
        
    def test_receps_recipe_template_load_is_correct(self):
    
        response = self.client.get(reverse('receps:receps-recipe', kwargs={'slug': 'test-recipe'}))       
        self.assertTemplateUsed(response, 'pages/recipe.html')