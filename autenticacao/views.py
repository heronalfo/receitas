from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from datetime import timedelta
from random import randrange
from . import forms

def cadastro(request):
    
    if request.method == "GET":
        form = forms.UsersForm()
        return render(request, 'cadastro.html', {'form': form})
    elif request.method == "POST":
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        senha2 = request.POST.get('senha2')

        if email in User.objects.values_list('email', flat=True):
            return render(request, 'cadastro.html', {'form': forms.UsersForm(), 'status': '1'})
        if senha != senha2:
            return render(request, 'cadastro.html', {'form': forms.UsersForm(), 'status': '2'})

        request.session['usuario'] = {'email': email, 'senha': senha}
        
        return redirect('/auth/validacao/')


def logar(request):
    
    if request.method == 'GET':
        return render(request, 'login.html', {'form': forms.UsersForm()})
    elif request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if not email or not senha:
            return HttpResponse('E-mail e senha sÃ£o obrigatÃ³rios.')

        user = authenticate(request, email=email, password=senha)

        if not user:
            login(request, user)
            return redirect('/plataforma/home/')
        else:        
            
            return render(request, 'login.html', {'form': forms.UsersForm(), 'status': '1'})


def validacao(request):
    
    if request.method == 'GET':
        email = request.session.get('usuario', {}).get('email')
        senha = request.session.get('usuario', {}).get('senha')

        if not email or not senha:
            return redirect('/auth/cadastro/')

        token = request.session.get('token_validacao_email', {}).get('token')

        if not token:
            token = randrange(100_000_000, 999_999_999)
            novo_token = str(token)
            tempo_expiracao = (timezone.now() + timedelta(seconds=60*30)).strftime('%Y-%m-%dT%H:%M:%S')
            
            request.session['token_validacao_email'] = {'token': str(novo_token), 'tempo': tempo_expiracao}
        else:
            token = request.session.get('token_validacao_email', {}).get('token')

        return render(request, 'validacao_email.html', {'email': email, 'token': token})

    elif request.method == 'POST':
        entrada_token = request.POST.get('token')
        email = request.session.get('usuario', {}).get('email')
        senha = request.session.get('usuario', {}).get('senha')
        token = request.session.get('token_validacao_email', {}).get('token')

        if not email or not senha or not token:
            return render(request, 'cadastro.html')

        elif entrada_token != token:
            return render(request, 'validacao_email.html', {'email': email, 'status': '2'})
        else:
        
            User.objects.create_user(username=email, password=senha)
        
            user = authenticate(request, username=email, password=senha)
            
            print('user:', user)

            if not user:
            
                return render(request, 'validacao_email.html', {'email': email, 'status': '0'})
            else:
            
                login(request, user)
                return redirect('/noticias/')
                
def reenviar(request):
 
    if request.method == 'GET':
    
        token = request.session.get('token_validacao_email', {}).get('token')
        
        novo_token = randrange(100_000_000, 999_999_999)
        
        tempo_expiracao = (timezone.now() + timedelta(seconds=60*30)).strftime('%Y-%m-%dT%H:%M:%S')
        
        request.session['token_validacao_email'] = {'token': str(novo_token), 'tempo': tempo_expiracao}
        
        return redirect('/auth/validacao/')