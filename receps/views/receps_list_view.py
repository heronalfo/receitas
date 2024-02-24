from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.views import View
from ..models import Receps, Categories
from ..utils import pagination
import os

PERPAGE = int(os.environ.get('PERPAGE', 1))

class RecepsListView(ListView):

    model = Receps
    context_object_name = 'Receps'
    ordering = ['-id']
    template_name = 'pages/receps.html'
      
    @staticmethod 
    def get_recepe_by_id(id: int):
               
        recepe = Receps.objects.all()
        recepe.filter(id=id)
        
        return recepe
    
    @staticmethod      
    def get_recepe_by_slug(slug):
        
        recepe = Receps.objects.all()
        recepe.filter(slug=slug)
        
        return recepe
    
    def get_queryset(self, *args, **kwargs):
    
        qs = super().get_queryset(*args, **kwargs)
        qs.filter(is_published=True)
        
        return qs
        
    def get_context_data(self, *args, **kwargs):
    
        ctx = super().get_context_data(*args, **kwargs)
    
        page_obj, pages = pagination.make_pagination(
        
            self.request,
            ctx.get('Receps'),
            PERPAGE, 1
        
        )
        
        ctx.update(
        
            {'page_obj': page_obj, 'pages': pages}
        )
        
        return ctx

class CategoryListView(RecepsListView):
    
    template_name = 'pages/category.html'
    
    def get_queryset(self, **kwargs):
                                         
        self.category = Categories.objects.get(name=self.kwargs["name"])
        
                       
        qs = super().get_queryset(**kwargs)
        
        qs.filter(category=self.category.id, is_published = True)
        
        return qs
    
    def get_context_data(self, **kwargs):
                
        ctx = super().get_context_data(**kwargs)
        
        ctx.update({'category_name': self.category.name, 'icon': self.category.icon})
        
        return ctx

class RecepeView(RecepsListView):
        
    def get(self, request, slug):
        
        try:
                    
            receps_list = self.get_recepe_by_slug(slug).first()
             
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

class SearchView(View):
    
    def post(self, *args):
        
        search = self.request.POST.get('search').strip()
        
        receps_list = Receps.objects.all().filter(
        
            Q(title__icontains=search) |
            Q(description__icontains=search) &
            Q(is_published=True)
        
        )
        
       
        query_params = self.request.GET.copy()
        
        query_params['search'] = search
        
        page_number = self.request.GET.get('page', 1)
       
        page_obj, pages = pagination.make_pagination(self.request, receps_list, PERPAGE, page_number)

        return render(self.request, 'pages/receps.html', {'Receps': page_obj, 'pages': pages, 'add': query_params['search']})
    
    def get(self, *args):
        
        return redirect(reverse('receps:receps'))
        
        