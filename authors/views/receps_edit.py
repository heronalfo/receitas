from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from receps.models import Receps, Categories
from ..forms import FormsAuthors


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