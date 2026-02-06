from django.db import models

# Create your models here.

class Match(models.Model):
    MATCH_TYPE_CHOICES = [
        ("League", "League"),
        ("Cup", "Cup"),
        ("Friendly", "Friendly"),
    ]

    VENUE_TYPE_CHOICES = [
        ("Home", "Home"),
        ("Away", "Away"),
        ("Neutral", "Neutral"),
    ]

    opponent_name = models.CharField(max_length=100)
    match_date = models.DateField()
    match_type = models.CharField(max_length=10, choices=MATCH_TYPE_CHOICES)
    venue_type = models.CharField(max_length=10, choices=VENUE_TYPE_CHOICES)
    location = models.CharField(max_length=150)
    our_score = models.IntegerField()
    opponent_score = models.IntegerField()

    def __str__(self):
        return f"{self.opponent_name} ({self.match_date})"


class Training(models.Model):
    TRAINING_TYPE_CHOICES = [
        ("Attacking", "Attacking"),
        ("Defending", "Defending"),
        ("Passing", "Passing"),
        ("Fitness", "Fitness"),
        ("Match Sim", "Match Sim"),
    ]

    training_date = models.DateField()
    duration = models.IntegerField() 
    training_type = models.CharField(max_length=15, choices=TRAINING_TYPE_CHOICES)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.training_type} ({self.training_date})"


class MatchAppearance(models.Model):

    player = models.ForeignKey("accounts.Player", on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)

    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    minutes_played = models.IntegerField(default=0)

    class Meta:
        unique_together = ("player", "match")

    def __str__(self):
        return f"{self.player} in {self.match}"


class TrainingAttendance(models.Model):
    player = models.ForeignKey("accounts.Player", on_delete=models.CASCADE)
    training = models.ForeignKey(Training, on_delete=models.CASCADE)

    is_present = models.BooleanField(default=True)
    player_notes = models.TextField(blank=True)

    class Meta:
        unique_together = ("player", "training")

    def __str__(self):
        return f"{self.player} - {self.training}"
