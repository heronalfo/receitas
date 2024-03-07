#pylint:disable=W0611

from django.views.generic import ListView
from django.views import View
from django.urls import reverse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from authors.models import Authors
from receps.models import Recipes, User
from ..forms import FormsAuthorsEdit
from receps.views import RecipesListView
import pdb                                                 
class AuthorsProfile(RecipesListView):

    template_name = 'pages/profile.html'                   
    def get_queryset(self, *args, **kwargs):               
        qs = super().get_queryset(*args, **kwargs)

        self.user_infos = User.objects.all().filter(username=self.kwargs["username"]).first()

        qs = qs.filter(user_id=self.user_infos.id)
        
        # qs = qs.prefetch_related('authors', 'user')


        return qs

    def get_context_data(self, *args, **kwargs):

        author = Authors.objects.all().filter(user_id=self.user_infos.id).first()

        ctx = super().get_context_data(*args, **kwargs)    
        ctx["user_infos"] = self.user_infos
        ctx["author"] = author
        ctx["total_revenue"] = self.get_queryset().count()
        
        print(ctx, author, self.user_infos)

        return ctx
        
@method_decorator(login_required(login_url='auth:login'), name='dispatch')
class AuthorsProfileEdit(View):

    def get(self, *args):
    
        form = FormsAuthorsEdit(
        
            self.request.POST or None,
            instance=Authors.objects.get(id=self.request.user.id)        
        )
        
        return render(
        
            self.request,
            
            'pages/profile_edit.html',
            
              {
              
                  'form': form,
              
              }
        )

    def post(self, *args):
    
        author = Authors.objects.get(user_id=self.request.user.id)
        
        author.name = self.request.POST.get('name')
        
        author.bio = self.request.POST.get('bio')
        
        author.link = self.request.POST.get('link')
        
        author.save()
        
        return redirect(reverse('authors:profile', args=(self.request.user.username, )))