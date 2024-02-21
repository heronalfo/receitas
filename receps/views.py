from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import QueryDict
from .models import Receps, Categories
from .utils import pagination
import os
import pdb

PERPAGE = int(os.environ.get('PERPAGE', 1))

def receps(request):

    receps_list = Receps.objects.all().filter(is_published=True).order_by('-id')
    
    page_obj, pages = pagination.make_pagination(request, receps_list, PERPAGE, 1)
    
       
    return render(request, 'pages/receps.html', {'Receps': page_obj, 'pages': pages})

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
    
    category = Categories.objects.all().filter(name=name).first()
            
    receps_list = Receps.objects.all().filter(category=category.id, is_published=True).order_by('-id')
     
    category = receps_list.first().category
    
    page_obj, pages = pagination.make_pagination(request, receps_list, PERPAGE, 1)
    
               
    return render(request, 'pages/category.html', {'Receps': page_obj, 'pages': pages, 'name_of_category': category.name, 'icon': category.icon})
    

def search(request):
    if request.method == 'POST':
    
        search = request.POST.get('search').strip()
        
        receps_list = Receps.objects.all().filter(
        
            Q(title__icontains=search) |
            Q(description__icontains=search) &
            Q(is_published=True)
        
        )
        
       
        query_params = request.GET.copy()
        
        query_params['search'] = search
        
        page_number = request.GET.get('page', 1)
       
        page_obj, pages = pagination.make_pagination(request, receps_list, PERPAGE, page_number)

        return render(request, 'pages/receps.html', {'Receps': page_obj, 'pages': pages, 'add': query_params['search']})
        
    elif request.method == 'GET':
        return redirect(reverse('receps:receps'))