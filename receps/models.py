from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Categories(models.Model):

    name = models.CharField(null=True, blank=True, max_length=38, unique=True)
    
    icon = models.CharField(default="fas fa-utensils",null=True, blank=True, max_length=100)
    
    def __str__(self):
        return self.name
     
class Recipes(models.Model):
    
    title = models.CharField(max_length=42)

    date = models.DateTimeField(auto_now_add=True)
    
    category = models.ForeignKey(Categories, on_delete=models.DO_NOTHING)
    
    portions = models.PositiveIntegerField(null=False, blank=False)
    
    user = models.ForeignKey(User, models.DO_NOTHING)
    
    description = models.TextField(blank=False)
    
    time = models.CharField(max_length=8)
    
    slug = models.SlugField(blank=True, null=False, unique=True)
    
    update = models.DateTimeField(auto_now=True)
    
    is_published = models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            # Gerar o slug com base no título
            self.slug = slugify(self.title)
            count = 0
            
            # Verificar se o slug já existe e incrementar um número se necessário
            while Recipes.objects.filter(slug=self.slug).exists():
                count += 1
                self.slug = f"{slugify(self.title)}-{count}"
            
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
            
            