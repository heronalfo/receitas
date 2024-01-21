from django.shortcuts import render
from .models import Receps

def receps(request):

    receps_list = Receps.objects.all()
    
    return render(request, 'pages/receps.html', {'Receps': receps_list})

def recipe(request, id):

    receps_list = Receps.objects.all().filter(id=id)[0]
    
    print(receps_list)
    
    return render(request, 'pages/recipe.html', {'recipe': receps_list})

def category(request, id):

    receps_list = Receps.objects.all().filter(category=id)
    
    return render(request, 'pages/receps.html', {'Receps': receps_list})


