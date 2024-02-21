from django.test import TestCase
from .. import models

class TestsAuthorsBase(TestCase):
                            
   
    
    def setUp(self):
       
        self.author = models.Authors(
        
            name = 'usertest',
            user = self.make_user(),
            bio = 'Bio',
            link = 'https://test.com'
            
            
        
        )
    
    def make_user(self, password="password", is_superuser=0, username="usertest", last_name="", email="usertest@gmail.com", is_staff=0, is_active=1, first_name=""):
    
        return models.User.objects.create(
            password=password,
            is_superuser=is_superuser,
            username=username,
            last_name=last_name,
            email=email,
            is_staff=is_staff,
            is_active=is_active,
            first_name=first_name
        )
    