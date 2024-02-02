from django.shortcuts import render
from .models import Authors
from receps.models import Receps, User

def profile(request, username):

    user = User.objects.all().filter(username=username).first()
    
    author = Authors.objects.all().filter(user_id=user.id).first()
    
          
    receps = Receps.objects.all().filter(user=user.id)
    
    revenue_total = receps.count()
    
    assert receps is not None
    assert author is not None
    

    return render(request, 'pages/profile.html', {'user': user,'author': author, 'total_revenue': revenue_total})