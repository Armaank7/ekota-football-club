from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.models import Staff, Player
from django.shortcuts import render, redirect

# @login required makes sure that you can only access this confidential page if you are signed in - prevents unauthorised access 
@login_required 
def staff_players_hub(request):

    # Ensure only staff can access this page
    if not Staff.objects.filter(user=request.user).exists():
        return redirect("LandingPage")

    if request.method == "POST":

        # CREATE PLAYER
        if "first_name" in request.POST:
            first_name = request.POST.get("first_name").strip()
            last_name = request.POST.get("last_name").strip()
            date_of_birth = request.POST.get("date_of_birth")
            position = request.POST.get("position")

            # Blank field check
            if first_name == "" or last_name == "" or date_of_birth == "" or position == "":
                messages.error(request, "All fields must be entered")
                return redirect("StaffPlayersHub")

            # Duplicate check to avoid adding the same player twice
            if Player.objects.filter(
                first_name=first_name,
                last_name=last_name,
                date_of_birth=date_of_birth
            ).exists():
                messages.error(request, "This player already exists")
                return redirect("StaffPlayersHub")

            # CREATE PLAYER
            Player.objects.create(
                first_name=first_name,
                last_name=last_name,
                date_of_birth=date_of_birth,
                position=position
            )

            messages.success(request, "Player created successfully!")
            return redirect("StaffPlayersHub")

        # DELETE PLAYER
        elif "deletePlayerID" in request.POST:
            player_id = request.POST.get("deletePlayerID")
            Player.objects.filter(id=player_id).delete()
            messages.success(request, "Player deleted")
            return redirect("StaffPlayersHub")

    # Order by player ID
    players = Player.objects.all().order_by("id")
    return render(request, "staff_players_hub.html", {
        "players": players
    })


@login_required
def update_player(request, player_id):

    # Ensure only staff can access
    if not Staff.objects.filter(user=request.user).exists():
        return redirect("LandingPage")

    player = Player.objects.get(id=player_id)

    if request.method == "POST":
        first_name = request.POST.get("first_name").strip()
        last_name = request.POST.get("last_name").strip()
        date_of_birth = request.POST.get("date_of_birth")
        position = request.POST.get("position")

        # Blank field check 
        if first_name == "" or last_name == "" or date_of_birth == "" or position == "":
            messages.error(request, "All fields must be entered")
            return redirect("UpdatePlayer", player_id=player.id)

        player.first_name = first_name
        player.last_name = last_name
        player.date_of_birth = date_of_birth
        player.position = position
        player.save()

        messages.success(request, "Player updated successfully!")
        return redirect("StaffPlayersHub")

    return render(request, "update_player.html", {"player": player})
