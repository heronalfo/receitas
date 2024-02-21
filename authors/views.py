from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.urls import reverse
from .models import Authors
from .forms import FormsAuthors
from receps.models import Receps, Categories, User
from datetime import datetime
import pdb

def profile(request, username):

    user_infos = User.objects.all().filter(username=username).first()
    
    author = Authors.objects.all().filter(user_id=user_infos.id).first()
             
    receps_list = Receps.objects.all().filter(is_published=True, user_id=user_infos.id).order_by('-id')
        
    revenue_total = receps_list.count()
    
    return render(request, 'pages/profile.html', {'user_infos': user_infos, 'author': author, 'total_revenue': revenue_total, 'Receps': receps_list})
    
@login_required(login_url='auth:login')
def dashboard(request):

    if request.method == 'GET':
    
        receps_list = Receps.objects.all().filter(user_id=request.user).order_by('-id')
    
        return render(request, 'pages/dashboard.html', {'Receps': receps_list})

@login_required(login_url='auth:login')
def create(request):


    if request.method == 'GET':
    
        form = FormsAuthors()
        now = datetime.now()
        
        return render(request, 'pages/form_create.html', {'form': form, 'date': now.date, 'receps_user': request.user})
    
    if request.method == 'POST':
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

@login_required(login_url='auth:login')        
def edit(request, id):
    
    if request.method == 'GET':
    
        form = FormsAuthors(
        
            request.POST or None,
            instance = Receps.objects.all().filter(id=id).first()
        
        )
        
        receps_list = Receps.objects.all().filter(id=id)
               
        return render(request, 'pages/form.html', {'form': form, 'Receps': receps_list})
    
    if request.method == "POST":
    
        title = request.POST.get('title')
        user=request.user,
        category = int(request.POST.get('category'))
        portions = int(request.POST.get('portions'))
        description = request.POST.get('description')        
        is_published = request.POST.get('is_published')   
        time = request.POST.get('time')
        
        print(title, user, category, portions, description, time)
        
        category_instance = Categories.objects.get(id=category)
        
        
        receps = Receps.objects.get(id=id)

        receps.title = title
        receps.user = request.user
        receps.category = category_instance
        receps.portions = portions
        receps.description = description
        receps.is_published = True if is_published == 'on' else False
        receps.time = time
        
        receps.save()
        
        
        
                
        return redirect('authors:dashboard')
        
@login_required(login_url='auth:login')
def delete(request, id):

    if request.method == 'POST':
    
        recipe = Receps.objects.all().filter(user_id=request.user, id=id).first()
        
        recipe.delete()
    
        return redirect(reverse('authors:dashboard'))        