from django.urls import path
from . import views

urlpatterns = [
    path("staff/register/", views.staff_register, name="StaffRegister"),
    path("login/", views.login, name="Login"),
    path("logout/", views.logout_view, name="Logout"),
]
