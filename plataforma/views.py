from django.shortcuts import render
from .models import Receps

def receps(request):

    receps_list = Receps.objects.all()
    
    return render(request, 'pages/receitas.html', {'Receps': receps_list})