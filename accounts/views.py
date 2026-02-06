from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from .forms import StaffRegisterForm
from .models import Staff, Player
from django.shortcuts import redirect
from django.contrib.auth import logout


# Create your views here.


def staff_register(request):
    if request.method == "POST":
        form = StaffRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            Staff.objects.create(user=user) 
            return redirect("LandingPage")
    else:
        form = StaffRegisterForm()

    return render(request, "staff_register.html", {"form": form})


def login(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        auth_login(request, user)

        if Staff.objects.filter(user=user).exists():
            return redirect("StaffHomepage")

        if Player.objects.filter(user=user).exists():
            return redirect("PlayerHomepage")

        return redirect("LandingPage")

    return render(request, "login.html", {"form": form})



def logout_view(request):
    logout(request)
    return redirect("LandingPage")