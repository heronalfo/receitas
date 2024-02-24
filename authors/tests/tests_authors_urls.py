from django.urls import reverse, resolve
from .tests_authors_base import TestsAuthorsBase

class AuthorsURLsTest(TestsAuthorsBase):    
    
    def test_authors_profile_url_is_correct(self):
        
        url = reverse('authors:profile', args=('pedro', ))
        self.assertEqual(url, '/authors/profile/pedro/')
    
    def test_authors_dashboard_url_is_correct(self):
        
        url = reverse('authors:dashboard')
        self.assertEqual(url, '/authors/dashboard/')
    
    def test_authors_edit_url_is_correct(self):
        
        url = reverse('authors:edit', args=(1, ))
        self.assertEqual(url, '/authors/dashboard/1/edit/')
    
    def test_authors_create_url_is_correct(self):
        
        url = reverse('authors:create')
        self.assertEqual(url, '/authors/dashboard/create/')
    
    def test_authors_delete_url_is_correct(self):
        
        url = reverse('authors:delete', args=(1, ))
        self.assertEqual(url, '/authors/dashboard/1/delete/')