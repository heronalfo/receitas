from django.shortcuts import render
from django.urls import reverse
from .models import Receps, Categories

def receps(request):

    receps_list = Receps.objects.all().filter(is_published=True).order_by('-id')
    
    return render(request, 'pages/receps.html', {'Receps': receps_list})

def recipe(request, slug):

    try:

        receps_list = Receps.objects.all().filter(slug=slug)[0]
    
    except:
    
        receps_list = {
        
            'title': 'Recipe not found', 
            'description': 'Name of recipe incorrect',
            'time': '0',
            'date': '00/00/00',
            'portions': 0,
            'slug': 'recipe-not-found-404'
            
        }
     
            
    return render(request, 'pages/recipe.html', {'recipe': receps_list})

def category(request, name):

    id_of_recipe = Categories.objects.all().filter(name=name)[0].id
    
    receps_list = Receps.objects.all().filter(category=id_of_recipe, is_published=True).order_by('-id')
    
    return render(request, 'pages/receps.html', {'Receps': receps_list})


