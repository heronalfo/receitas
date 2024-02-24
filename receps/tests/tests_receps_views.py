from django.urls import reverse, resolve
import pdb
from .tests_receps_base import TestsRecepsBase
from .. import views

class RecepsViewsTest(TestsRecepsBase):
    
    def test_receps_home_views_is_correct(self): 
    
        view = resolve(reverse('receps:receps'))
        self.assertIs(view.func.view_class, views.RecepsListView)
    
            
    def test_receps_recipe_views_is_correct(self):
           
        view = resolve(reverse('receps:receps-recipe', kwargs={'slug': 'test-recipe'}))
        self.assertIs(view.func.view_class, views.RecepeView)
        
    def test_receps_search_views_is_correct(self):
           
        view = resolve(reverse('receps:search'))
        
        self.assertIs(view.func.view_class, views.SearchView)