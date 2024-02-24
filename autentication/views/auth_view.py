from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth import authenticate, login as django_login
from django.contrib import messages
from django.contrib.auth.models import User
from django.views import View
from django.urls import reverse
from datetime import timedelta
from random import randrange
from .. import forms


class AuthRegister(View):

    
    def get(self, *args):
        
        form = forms.UsersForm()
        return render(self.request, 'pages/register.html', {'form': form})
        
        
    def post(self, *args):
        
        email = self.request.POST.get('email')
        
        password = request.POST.get('password')
        
        password_repeat = self.request.POST.get('password-repeat')

        if email in User.objects.values_list('email', flat=True):
            messages.error(self.request, 'This email is already registered')
            
        if password != password_repeat:
            messages.error(self.request, 'email and password must be equal')
        
        if messages.get_messages(self.request):
            form = forms.UsersForm(self.request.POST)
            
            return render(self.request, 'pages/register.html', {'form': form})
        
        user_cookie = {'email': email, 'password': password}
                        
        self.request.session['user_cookie'] = user_cookie
                        
        return redirect(reverse('auth:validation'))


class AuthLogin(View): 
    
    def get(self, *args):
        
        form = forms.UsersForm()
    
        return render(self.request, 'pages/login.html', {'form': form})
        
    def post(self, *args):
    
        email = self.request.POST.get('email')
        
        password = self.request.POST.get('password')
        
        user = authenticate(request, email=email, password=password)

        if not user:
            django_login(self.request, user)
            
            return redirect(reverse('receps:receps'))
            
        else:                    
            messages.error(self.request, 'email or password are incorrect')


class AuthValidation(View):
    
    def get(self, *args):
        
        email = self.request.session.get('user_cookie', {}).get('email')
        
        password = self.request.session.get('user_cookie', {}).get('password')
        
        print(email, password)

        if not email or not password:
            return redirect(reverse('auth:register'))

        token = self.request.session.get('token_validation_email', {}).get('token')

        if not token:
            token = randrange(100_000_000, 999_999_999)
            
            novo_token = str(token)
            
            time_expiration = (timezone.now() + timedelta(seconds=60*30)).strftime('%Y-%m-%dT%H:%M:%S')
            
            self.request.session['token_validation_email'] = {'token': str(novo_token), 'time': time_expiration}
            
        else:
            token = request.session.get('token_validation_email', {}).get('token')
            
        print(email, token)

        return render(self.request, 'pages/validation.html', {'email': email, 'token': token})

    def post(self, *args):
        entrada_token = self.request.POST.get('token')
        
        email = self.request.session.get('user_cookie', {}).get('email')
        
        password = self.request.session.get('user_cookie', {}).get('password')
        
        token = self.request.session.get('token_validation_email', {}).get('token')

        if not email or not password or not token:
            return render(self.request, 'pages/register.html')

        elif entrada_token != token:
            messages.error(self.request, 'The token insert are incorrect')
            
        else:        
            User.objects.create_user(username=email, password=password)
        
            user = authenticate(self.request, username=email, password=password)
            
           
            if not user:            
                return render(self.request, 'pages/validation.html', {'email': email, 'status': '0'})
                
            else:                
                django_login(self.request, user)
                
                return redirect(reverse('receps:receps'))
                
class AuthResend(View):
 
    def get(self, *args):
    
        token = self.request.session.get('token_validation_email', {}).get('token')
        
        if not token:
        
            return redirect(reverse('auth:register'))
        
        novo_token = randrange(100_000_000, 999_999_999)
        
        time_expiration = (timezone.now() + timedelta(seconds=60*30)).strftime('%Y-%m-%dT%H:%M:%S')
        
        request.session['token_validation_email'] = {'token': str(novo_token), 'time': time_expiration}
        
        return redirect(reverse('auth:validation/'))