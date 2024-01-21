from django.db import models
from django.contrib.auth.models import User

class Categories(models.Model):

    name = models.CharField(null=True, blank=True, max_length=38)

class Receps(models.Model):

    title = models.CharField(max_length=92)
    
    date = models.DateTimeField(auto_now_add=True)
    
    category = models.ForeignKey(Categories, on_delete=models.DO_NOTHING)
    
    portions = models.IntegerField()
    
    user = models.ForeignKey(User, models.DO_NOTHING)
    
    description = models.TextField()
    
    time = models.CharField(max_length=192)
    
    slug = models.SlugField()
    
    update = models.DateTimeField(auto_now=True)