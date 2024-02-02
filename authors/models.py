from django.db import models
from receps.models import Receps, User

class Authors(models.Model):

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    
    name = models.CharField(max_length=12, null=True, blank=False)
    
    bio = models.CharField(max_length=100, null=True, blank=True)
    
    link = models.CharField(max_length=100, null=True, blank=False)
    
    stars = models.IntegerField(default=0)
    
    is_professional = models.IntegerField(default=0)
    
    #image
    
    
    
    
    
