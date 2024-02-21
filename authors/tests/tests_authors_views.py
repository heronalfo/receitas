from django.urls import reverse, resolve
import pdb
from .tests_authors_base import TestsAuthorsBase
from .. import views

class AuthorsViewsTest(TestsAuthorsBase):
    
    def test_authors_profile_views_is_correct(self): 
    
        view = resolve(reverse('authors:profile', args=('pedro', )))
        self.assertIs(view.func, views.profile)