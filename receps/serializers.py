from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Recipes, Categories

class RecipesModelsSerializer(serializers.ModelSerializer):

    class Meta:    
    
        model = Recipes
        
        fields = ['id', 'title', 'description', 'portions', 'time', 'slug', 'user', 'category']

        
    user = serializers.PrimaryKeyRelatedField(
    
      queryset=User.objects.all()
    )
        
    category = serializers.StringRelatedField(
      read_only=True
    )
   