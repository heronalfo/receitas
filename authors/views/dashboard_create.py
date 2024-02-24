from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator
from django.urls import reverse

from datetime import datetime
from ..models import Authors
from ..forms import FormsAuthors
from receps.models import Receps, Categories
import pdb

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
            
        category = int(request.POST.get('category'))
            
                                
        category_instance = Categories.objects.get(id=category)
    
        Receps(
       
            title= request.POST.get('title'),
                
            user=request.user,
                
            category =category_instance,
              
            portions = int(request.POST.get('portions')),
                
            description = request.POST.get('description'),
                
            is_published=True if is_published == 'on' else False,
            
            time = request.POST.get('time')
                    
        ).save()
        
        return redirect(reverse('authors:dashboard'))
    
        