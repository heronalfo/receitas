from django.urls import reverse, resolve
import pdb
from .tests_recipes_base import TestRecipesBase
from .. import views

class RecipesViewsTest(TestRecipesBase):
    
    def test_recipes_home_views_is_correct(self): 
    
        view = resolve(reverse('recipes:recipes'))
        self.assertIs(view.func.view_class, views.RecipesListView)
    
            
    def test_recipes_recipe_views_is_correct(self):
           
        view = resolve(reverse('recipes:recipes-recipe', kwargs={'slug': 'test-recipe'}))
        self.assertIs(view.func.view_class, views.RecipeView)
        
    def test_recipes_search_views_is_correct(self):
           
        view = resolve(reverse('recipes:search'))
        
        self.assertIs(view.func.view_class, views.RecipesSearchView)