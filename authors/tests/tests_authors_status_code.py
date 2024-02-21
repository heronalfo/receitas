from django.urls import reverse, resolve
from .tests_authors_base import TestsAuthorsBase
from time import sleep
import pdb

class AuthorsStatusCodeTest(TestsAuthorsBase):

    def test_authors_profile_status_code_is_200(self):
        
        response = self.client.get(reverse('authors:profile', args=('usertest', )))
                               
        self.assertEqual(response.status_code, 200)