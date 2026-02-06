from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def landing_page(request):
    return render(request, "landing.html")

def staff_homepage(request):
    return render(request, "staff_homepage.html")

def player_homepage(request):
    return render(request, "player_homepage.html")
