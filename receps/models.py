from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Categories(models.Model):

    name = models.CharField(null=True, blank=True, max_length=38, unique=True)

class Receps(models.Model):

    title = models.CharField(max_length=92)
    
    date = models.DateTimeField(auto_now_add=True)
    
    category = models.ForeignKey(Categories, on_delete=models.DO_NOTHING)
    
    portions = models.IntegerField()
    
    user = models.ForeignKey(User, models.DO_NOTHING)
    
    description = models.TextField()
    
    time = models.CharField(max_length=192)
    
    slug = models.SlugField(blank=True, null=False, unique=True)
    
    update = models.DateTimeField(auto_now=True)
    
    is_published = models.BooleanField(default=True)
    
    from django.utils.text import slugify

class Receps(models.Model):
    
    title = models.CharField(max_length=92)

    date = models.DateTimeField(auto_now_add=True)
    
    category = models.ForeignKey(Categories, on_delete=models.DO_NOTHING)
    
    portions = models.IntegerField()
    
    user = models.ForeignKey(User, models.DO_NOTHING)
    
    description = models.TextField()
    
    time = models.CharField(max_length=192)
    
    slug = models.SlugField(blank=True, null=False, unique=True)
    
    update = models.DateTimeField(auto_now=True)
    
    is_published = models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            # Gerar o slug com base no título
            self.slug = slugify(self.title)
            count = 0
            
            # Verificar se o slug já existe e incrementar um número se necessário
            while Receps.objects.filter(slug=self.slug).exists():
                count += 1
                self.slug = f"{slugify(self.title)}-{count}"
            
        super().save(*args, **kwargs)
            
            