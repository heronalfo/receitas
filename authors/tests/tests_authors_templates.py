from django.test import TestCase
from django.urls import reverse
from .tests_authors_base import TestsAuthorsBase

class AuthorsTemplatesTest(TestsAuthorsBase):

    def test_authors_profile_template_load_is_correct(self):
    
        response = self.client.get(reverse('authors:profile', args=('usertest',)))        
        self.assertTemplateUsed(response, 'pages/profile.html')