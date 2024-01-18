from django.db import models
from django.contrib.auth.models import User

class Receps(models.Model):

    title = models.CharField(null=False, blank=False, max_length=92)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    date = models.DateField(null=False, blank=False)
    
    description = models.TextField(null=False, blank=False)
    
    CATEGORYS = [
    
    ('breakfast', 'Breakfast'),
    ('lunch', 'Lunch'),
    ('dinner', 'Dinner'),
    
    ]
    
    category = models.CharField(choices=CATEGORYS, null=False, blank=False, max_length=102)
    
    time = models.CharField(null=False, blank=False, max_length=192)
    
    portions = models.IntegerField(null=False, blank=False)
    
    
    