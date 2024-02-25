from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

from django.utils.decorators import method_decorator
from django.urls import reverse

from datetime import datetime
from ..models import Authors
from ..forms import FormsAuthors
from receps.models import Recipes, Categories
from receps.views import RecipesListView
import pdb

@method_decorator(login_required(login_url='auth:login'), name='dispatch')
class AuthorsDashboard(RecipesListView):
    """
    View for the author's dashboard.
    """
    template_name = 'pages/dashboard.html'
    ordering = ["-id"]
    
    def get_queryset(self, *args, **kwargs):
        """
        Return the queryset of unpublished recipes by the current user.

        Returns:
            queryset: Queryset object containing the unpublished recipes by the current user.
        """
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(is_published=False, user_id=self.request.user)
        return qs
    

@method_decorator(login_required(login_url='auth:login'), name='dispatch')
class AuthorsCreate(View):
    """
    View for creating a new recipe by the author.
    """
    def get(self, request):
        """
        Handle GET requests for creating a new recipe.
        """
        form = FormsAuthors()
        now = datetime.now()
        return render(
            request,
            'pages/form_create.html',
            {
                'form': form,
                'date': now.date,
                'recipes_user': request.user
            }
        )
    
    def post(self, request):
        """
        Handle POST requests for creating a new recipe.
        """
        form = FormsAuthors()
        title = request.POST.get('title')
        user = request.user
        category = int(request.POST.get('category'))
        portions = int(request.POST.get('portions'))
        description = request.POST.get('description')
        is_published = request.POST.get('is_published')
        time = request.POST.get('time')
        
        category_instance = Categories.objects.get(id=category)

        Recipes(
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
class AuthorsRecipeEdit(View):
    """
    View for editing an existing recipe by the author.
    """
    def get(self, request, id):
        """
        Handle GET requests for editing an existing recipe.
        """
        self.recipe = Recipes.objects.filter(id=id)
        self.form = FormsAuthors(
            request.POST or None,
            instance=self.recipe.first()
        )
        return render(request, 'pages/form.html', {'form': self.form, 'recipes': self.recipe})
   
    def post(self, request, id):
        """
        Handle POST requests for editing an existing recipe.
        """
        category = int(request.POST.get('category'))
        recipe = Recipes.objects.get(id=id)
        
        recipe.title = request.POST.get('title')
        category_instance = Categories.objects.get(id=category)
        recipe.category = category_instance
        recipe.portions = request.POST.get('portions')
        recipe.description = request.POST.get('description')
        recipe.time = request.POST.get('time')
        recipe.save()
        
        return redirect(reverse('authors:dashboard'))

class AuthorsRecipeDelete(View):
    """
    View for deleting an existing recipe by the author.
    """
    def post(self, *args, **kwargs):
        """
        Handle POST requests for deleting an existing recipe.
        """
        recipe = Recipes.objects.all().filter(id=self.kwargs["id"]).first()
        recipe.delete()
        return redirect(reverse('authors:dashboard'))