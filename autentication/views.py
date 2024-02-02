from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth import authenticate, login as django_login
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import timedelta
from random import randrange
from . import forms

def register(request):
    
    if request.method == "GET":
        form = forms.UsersForm()
        return render(request, 'pages/register.html', {'form': form})
    elif request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_repeat = request.POST.get('password-repeat')

        if email in User.objects.values_list('email', flat=True):
            messages.error(request, 'This email is already registered')
        if password != password_repeat:
            messages.error(request, 'email and password must be equal')
        
        if messages.get_messages(request):
            form = forms.UsersForm(request.POST)
            return render(request, 'pages/register.html', {'form': form})

        # Aqui você continua com o processamento se não houver mensagens de erro
        
        user_cookie = {'email': email, 'password': password}
                        
        request.session['user_cookie'] = user_cookie
                        
        return redirect(reverse('auth:validation'))  # Redirecionar após o registro


def login(request): 
    
    if request.method == 'GET':
        return render(request, 'pages/login.html', {'form': forms.UsersForm()})
    elif request.method == 'POST':
    
        email = request.POST.get('email')
        password = request.POST.get('password')
        

        user = authenticate(request, email=email, password=password)

        if not user:
            django_login(request, user)
            return redirect(reverse('receps:receps'))
        else:        
            
            messages.error(request, 'email or password are incorrect')


def validation(request):
    
    if request.method == 'GET':
        email = request.session.get('user_cookie', {}).get('email')
        password = request.session.get('user_cookie', {}).get('password')
        
        print(email, password)

        if not email or not password:
            return redirect(reverse('auth:register'))

        token = request.session.get('token_validation_email', {}).get('token')

        if not token:
            token = randrange(100_000_000, 999_999_999)
            novo_token = str(token)
            time_expiration = (timezone.now() + timedelta(seconds=60*30)).strftime('%Y-%m-%dT%H:%M:%S')
            
            request.session['token_validation_email'] = {'token': str(novo_token), 'time': time_expiration}
        else:
            token = request.session.get('token_validation_email', {}).get('token')
            
        print(email, token)

        return render(request, 'pages/validation.html', {'email': email, 'token': token})

    elif request.method == 'POST':
        entrada_token = request.POST.get('token')
        email = request.session.get('user_cookie', {}).get('email')
        password = request.session.get('user_cookie', {}).get('password')
        token = request.session.get('token_validation_email', {}).get('token')

        if not email or not password or not token:
            return render(request, 'pages/register.html')

        elif entrada_token != token:
            messages.error(request, 'The token insert are incorrect')
        else:
        
            User.objects.create_user(username=email, password=password)
        
            user = authenticate(request, username=email, password=password)
            
            print(user)

            if not user:
            
                return render(request, 'pages/validation.html', {'email': email, 'status': '0'})
            else:
            
                django_login(request, user)
                return redirect(reverse('receps:receps'))
                
def resend(request):
 
    if request.method == 'GET':
    
        token = request.session.get('token_validation_email', {}).get('token')
        
        if not token:
        
            return redirect(reverse('auth:register'))
        
        novo_token = randrange(100_000_000, 999_999_999)
        
        time_expiration = (timezone.now() + timedelta(seconds=60*30)).strftime('%Y-%m-%dT%H:%M:%S')
        
        request.session['token_validation_email'] = {'token': str(novo_token), 'time': time_expiration}
        
        return redirect(reverse('auth:validation/'))