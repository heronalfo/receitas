from django.urls import reverse, resolve
from .tests_authors_base import TestsAuthorsBase

class AuthorsURLsTest(TestsAuthorsBase):    
    
    def test_authors_profile_url_is_correct(self):
        
        url = reverse('authors:profile', args=('pedro', ))
        self.assertEqual(url, '/authors/profile/pedro/')