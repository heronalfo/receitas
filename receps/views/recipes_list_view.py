from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.http import JsonResponse
from django.views import View
from ..models import Recipes, Categories
from ..utils import pagination
import os

PERPAGE = int(os.environ.get('PERPAGE', 1))

class RecipesListView(ListView):
    """
    View to list recipes.
    """
    model = Recipes
    context_object_name = 'recipes'
    ordering = ['-id']
    template_name = 'pages/recipes.html'
      
    @staticmethod 
    def get_recipe_by_id(id: int):
        """
        Retrieve a recipe by ID.

        Args:
            id (int): The ID of the recipe to retrieve.

        Returns:
            queryset: Queryset object containing the recipe with the specified ID.
        """
        recipes = Recipes.objects.all()
        recipes.filter(id=id)
        
        return recipes
    
    @staticmethod      
    def get_recipe_by_slug(slug):
        """
        Retrieve a recipe by slug.

        Args:
            slug (str): The slug of the recipe to retrieve.

        Returns:
            queryset: Queryset object containing the recipe with the specified slug.
        """
        recipes = Recipes.objects.all()
        recipes.filter(slug=slug)
        
        return recipes
    
    def get_queryset(self, *args, **kwargs):
        """
        Return the queryset of recipes filtered by published recipes.

        Returns:
            queryset: Queryset object containing the published recipes.
        """
        qs = super().get_queryset(*args, **kwargs)
        qs.filter(is_published=True)
        
        qs = qs.prefetch_related('user', 'category')
        
        return qs
        
    def get_context_data(self, *args, **kwargs):
        """
        Return the data context for the recipes page.

        Returns:
            dict: Dictionary containing the data context for the recipes page.
        """
        ctx = super().get_context_data(*args, **kwargs)
    
        page_obj, pages = pagination.make_pagination(
            self.request,
            ctx.get('recipes'),
            PERPAGE, 1
        )
        
        ctx.update({'page_obj': page_obj, 'pages': pages})
        
        return ctx

class CategoryListView(RecipesListView):  
    """
    View to list recipes by category.
    """
    template_name = 'pages/category.html'
    
    def get_queryset(self, **kwargs):
        """
        Return the queryset of recipes filtered by category.

        Returns:
            queryset: Queryset object containing the recipes of the specified category.
        """
        
        try:
        
            self.category = Categories.objects.get(name=self.kwargs["name"])
            
        except:
        
            return None
            
        qs = super().get_queryset(**kwargs)
        qs.filter(category=self.category.id, is_published=True)
        
        return qs
    
    def get_context_data(self, **kwargs):
        """
        Return the data context for the category page.

        Returns:
            dict: Dictionary containing the data context for the category page.
        """
        
        ctx = super().get_context_data(**kwargs)
        
        if ctx is not None:
                
            ctx.update({'category_name': self.category.name, 'icon': self.category.icon})
            
            return ctx
            
        else:
        
            return redirect(reverse('recipes:recipes'))

class RecipeView(View):
    """
    View to display details of a recipe.
    """
    def get(self, *args, **kwargs):       
        try:
        
            recipe = Recipes.objects.get(slug=self.kwargs["slug"])
            
            return render(self.request, 'pages/recipe.html', {'recipe': recipe})
            
            return 
            
        except ValueError:
            recipe = {
                'title': 'Recipe not found', 
                'description': 'Name of recipe incorrect',
                'time': '0',
                'date': '00/00/00',
                'portions': 0,
                'slug': 'recipe-not-found-404'
            }
         
        return render(self.request, 'pages/recipe.html', {'recipe': recipe})

class RecipesSearchView(View):
    """
    View to search recipes.
    """
    def post(self, *args):       
        search = self.request.POST.get('search').strip()
        recipes = Recipes.objects.all().filter(
            Q(title__icontains=search) |
            Q(description__icontains=search) &
            Q(is_published=True)
        )
               
        query_params = self.request.GET.copy()
        query_params['search'] = search
        page_number = self.request.GET.get('page', 1)
        
        page_obj, pages = pagination.make_pagination(self.request, recipes, PERPAGE, page_number)
        
        return render(
        
        self.request,
        
        'pages/recipes.html',
            
          {
            
              'recipes': page_obj,
              'pages': pages,
        
              'add': query_params['search'],
              'search': search
            
          }
        )
    
    def get(self, *args):
        return redirect(reverse('recipes:recipes'))
        