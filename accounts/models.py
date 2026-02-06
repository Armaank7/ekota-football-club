from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    staffID = models.CharField(max_length=20, unique=True, blank=True, default="")

    def __str__(self):
        return f"Staff: {self.user.username}"


class Player(models.Model):
    POSITION_CHOICES = [   # List of possible position categories - represented as dropdown menu
        ("GK", "GK"),
        ("DEF", "DEF"),
        ("MID", "MID"),
        ("FWD", "FWD"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    playerID = models.CharField(max_length=20, unique=True, blank=True, default="")
    first_name = models.CharField(max_length=50, default="")
    last_name = models.CharField(max_length=50, default="")
    date_of_birth = models.DateField()
    position = models.CharField(max_length=3, choices=POSITION_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
