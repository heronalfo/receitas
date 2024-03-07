#pylint:disable=E0602
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Categories(models.Model):

    name = models.CharField(null=True, blank=True, max_length=38, unique=True)
    
    icon = models.CharField(default="fas fa-utensils",null=True, blank=True, max_length=100)
    
    def __str__(self):
        return self.name
     
class Recipes(models.Model):
    
    cover = models.ImageField(upload_to='images/', default='', null=True, blank=True)
    
    title = models.CharField(max_length=42)

    date = models.DateTimeField(auto_now_add=True)
    
    category = models.ForeignKey(Categories, on_delete=models.DO_NOTHING)
    
    portions = models.PositiveIntegerField()
    
    user = models.ForeignKey(User, models.DO_NOTHING)
    
    description = models.TextField()
    
    time = models.CharField(max_length=8)
    
    slug = models.SlugField(unique=True)
    
    update = models.DateTimeField(auto_now=True)
    
    is_published = models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            
            self.slug = slugify(self.title)
            count = 0
                        
            while Recipes.objects.filter(slug=self.slug).exists():
                count += 1
                self.slug = f"{slugify(self.title)}-{count}"
            
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
            
            