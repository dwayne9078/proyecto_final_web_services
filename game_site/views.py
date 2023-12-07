from django.shortcuts import render

from game_site.templates import *

# Create your views here.
def showLandingPage(request):
    return render(request, 'landing_page.html')

def showLogin(request):
    return render(request, 'login.html')