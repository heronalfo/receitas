from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.models import User
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
        password_repeat= request.POST.get('password-repeat')

        if email in User.objects.values_list('email', flat=True):
            return render(request, 'pages/register.html', {'form': forms.UsersForm(), 'status': '1'})
        if password != password_repeat:
            return render(request, 'pages/register.html', {'form': forms.UsersForm(), 'status': '2'})

        request.session['user_cookie'] = {'email': email, 'password': password}
        
        print(email, password)
        
        return redirect('/auth/validation/')


def login(request): 
    
    if request.method == 'GET':
        return render(request, 'pages/login.html', {'form': forms.UsersForm()})
    elif request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email or not password:
            return HttpResponse('E-mail e password sÃ£o obrigatÃ³rios.')

        user = authenticate(request, email=email, password=password)

        if not user:
            django_login(request, user)
            return redirect('/receps/')
        else:        
            
            return render(request, 'pages/login.html', {'form': forms.UsersForm(), 'status': '1'})


def validation(request):
    
    if request.method == 'GET':
        email = request.session.get('user_cookie', {}).get('email')
        password = request.session.get('user_cookie', {}).get('password')
        
        print(email, password)

        if not email or not password:
            return redirect('/auth/register/')

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
            return render(request, 'pages/validation.html', {'email': email, 'status': '2'})
        else:
        
            User.objects.create_user(username=email, password=password)
        
            user = authenticate(request, username=email, password=password)
            
            print(user)

            if not user:
            
                return render(request, 'pages/validation.html', {'email': email, 'status': '0'})
            else:
            
                django_login(request, user)
                return redirect('/receps/')
                
def resend(request):
 
    if request.method == 'GET':
    
        token = request.session.get('token_validation_email', {}).get('token')
        
        novo_token = randrange(100_000_000, 999_999_999)
        
        time_expiration = (timezone.now() + timedelta(seconds=60*30)).strftime('%Y-%m-%dT%H:%M:%S')
        
        request.session['token_validation_email'] = {'token': str(novo_token), 'time': time_expiration}
        
        return redirect('/auth/validation/')