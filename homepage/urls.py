from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing_page, name="LandingPage"),
    path("staff/homepage/", views.staff_homepage, name="StaffHomepage"),
    path("player/homepage/", views.player_homepage, name="PlayerHomepage"),
]
