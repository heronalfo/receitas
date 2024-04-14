from django.shortcuts import redirect
from django.urls import reverse

def recipes_handler404(request, exception):
    return redirect(reverse('recipes:recipes'))
    