from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from users.forms import *

# Create your views here.
def showLandingPage(request):
    return render(request, 'landing_page.html')

def showThanks(request):
    if request.user.is_authenticated:
        return render(request, 'thanks.html')
    else:
        return redirect("/")
        

def showLogin(request):
    if request.method == 'GET':
        return render(request, 'login.html', { 'form': LoginForm()})
    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            
        messages.error(request,f'Invalid username or password')
        return render(request,'login.html',{'form': form})

def showLogOut(request):
    logout(request)
    messages.success(request, "Cerrado sesion")
    return redirect('/')

def showRegister(request):
    return render(request, 'register.html')