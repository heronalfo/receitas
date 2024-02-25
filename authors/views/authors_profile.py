from django.views.generic import ListView
from django.urls import reverse
from django.shortcuts import render, redirect
from authors.models import Authors
from receps.models import Recipes, User
from receps.views import RecipesListView
import pdb                                                 
class AuthorsProfile(RecipesListView):

    template_name = 'pages/profile.html'                   
    def get_queryset(self, *args, **kwargs):               
        qs = super().get_queryset(*args, **kwargs)

        self.user_infos = User.objects.all().filter(username=self.kwargs["username"]).first()

        qs = qs.filter(user_id=self.user_infos.id)


        return qs

    def get_context_data(self, *args, **kwargs):

        author = Authors.objects.all().filter(user_id=self.user_infos.id).first()

        ctx = super().get_context_data(*args, **kwargs)    
        ctx["user_infos"] = self.user_infos
        ctx["author"] = author
        ctx["total_revenue"] = self.get_queryset().count()

        return ctx