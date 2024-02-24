from django.urls import reverse, resolve
import pdb
from .tests_authors_base import TestsAuthorsBase
from .. import views

class AuthorsViewsTest(TestsAuthorsBase):
    
    def test_authors_profile_views_is_correct(self): 
    
        view = resolve(reverse('authors:profile', args=('pedro', )))
        self.assertIs(view.func.view_class, views.AuthorsProfile)
    
    def test_authors_dashboard_views_is_correct(self):     
        view = resolve(reverse('authors:dashboard'))
        
        self.assertIs(view.func.view_class, views.AuthorsDashboard)
    
    def test_authors_create_views_is_correct(self): 
    
        view = resolve(reverse('authors:create'))
        self.assertIs(view.func.view_class, views.AuthorsCreate)
        
    def test_authors_edit_views_is_correct(self): 
    
        view = resolve(reverse('authors:edit', args=(1, )))
        
        self.assertIs(view.func.view_class, views.RecepsEdit)
    
    def test_authors_delete_views_is_correct(self): 
    
        view = resolve(reverse('authors:delete', args=(1, )))
        
        self.assertIs(view.func.view_class, views.AuthorsRecepeDelete)