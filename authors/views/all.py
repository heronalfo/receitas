from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.urls import reverse
from ..models import Authors
from ..forms import FormsAuthors
from receps.models import Receps, Categories, User
from datetime import datetime
import pdb
    
@login_required(login_url='auth:login')

def delete(request, id):

    if request.method == 'POST':
    
        recipe = Receps.objects.all().filter(user_id=request.user, id=id).first()
        
        recipe.delete()
    
        return redirect(reverse('authors:dashboard'))        