from django.urls import path
from . import views

urlpatterns = [
    path("staff/players/", views.staff_players_hub, name="StaffPlayersHub"),
    path("staff/players/<int:player_id>/update/", views.update_player, name="UpdatePlayer"),
]
