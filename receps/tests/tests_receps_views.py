from django.urls import reverse, resolve
import pdb
from .tests_receps_base import TestsRecepsBase
from .. import views

class RecepsViewsTest(TestsRecepsBase):
    
    def test_receps_home_views_is_correct(self): 
    
        view = resolve(reverse('receps:receps'))
        self.assertIs(view.func, views.receps)
    
    def test_receps_category_views_is_correct(self):   
    
        view = resolve(reverse('receps:category', kwargs={'name': 'BreakFast'}))        
        self.assertIs(view.func, views.category)
        
    def test_receps_recipe_views_is_correct(self):
           
        view = resolve(reverse('receps:receps-recipe', kwargs={'slug': 'test-recipe'}))
        self.assertIs(view.func, views.recipe)