from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

from django.utils.decorators import method_decorator
from django.urls import reverse

from datetime import datetime
from ..models import Authors
from ..forms import FormsAuthors
from receps.models import Receps, Categories
from receps.views import RecepsListView
import pdb

@method_decorator(login_required(login_url='auth:login'), name='dispatch')
class AuthorsDashboard(RecepsListView):
    
    template_name = 'pages/dashboard.html'
    ordering = ["-id"]
    
    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        
        qs = qs.filter(is_published=False, user_id = self.request.user)
        
        return qs
    

@method_decorator(login_required(login_url='auth:login'), name='dispatch')

class AuthorsCreate(View):

    def get(self, request):
    
        form = FormsAuthors()
        now = datetime.now()
        
        return render(
        
            request,
            'pages/form_create.html',
            
                {
                
                'form': form,                 
                'date': now.date,                 
                'receps_user': request.user
                }
                
        )
    
    
    def post(self, request):
    
        form = FormsAuthors()
                        
        title = request.POST.get('title')
        user=request.user,
        category = int(request.POST.get('category'))
        portions = int(request.POST.get('portions'))
        description = request.POST.get('description')        
        is_published = request.POST.get('is_published')   
        time = request.POST.get('time')
                            
        category_instance = Categories.objects.get(id=category)

        Receps(
    
            title=title,
            user=request.user,
            category=category_instance,
            portions=portions,
            description=description,
            is_published=True if is_published == 'on' else False,
            time=time    
                
        ).save()
        
        return redirect(reverse('authors:dashboard'))

@method_decorator(login_required(login_url='auth:login'), name='dispatch')

class RecepsEdit(View):
    
                       
    def get(self, request, id):
       
       self.receps = Receps.objects.filter(id=id)
       
       self.form = FormsAuthors(
        
        request.POST or None,
        instance = self.receps.first()
        
        )
       
       return render(request, 'pages/form.html', {'form': self.form, 'Receps': self.receps})
   
    def post(self, request, id):
        
        category = int(request.POST.get('category'))
        
        receps = Receps.objects.get(id=id)
                                     
        
        receps.title = request.POST.get('title')
                
        category_instance = Categories.objects.get(id=category)
        
        receps.category = category_instance
        
        receps.portions = request.POST.get('portions')
        
        receps.description = request.POST.get('description')
        
        receps.time = request.POST.get('time')
        
        receps.save()
        
        return redirect(reverse('authors:dashboard'))

class AuthorsRecepeDelete(View):

    def post(self, *args, **kwargs):
    
        recipe = Receps.objects.all().filter(id=self.kwargs["id"]).first()
        
        recipe.delete()
        
        return redirect(reverse('authors:dashboard'))
    
    
        