from django.db import models
from bson import ObjectId

class User(models.Model):
    _id = models.CharField(max_length=24, primary_key=True, default=lambda: str(ObjectId()), editable=False)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

class Team(models.Model):
    _id = models.CharField(max_length=24, primary_key=True, default=lambda: str(ObjectId()), editable=False)
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User, related_name='teams')

class Activity(models.Model):
    _id = models.CharField(max_length=24, primary_key=True, default=lambda: str(ObjectId()), editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=50)
    duration = models.DurationField()

class Leaderboard(models.Model):
    _id = models.CharField(max_length=24, primary_key=True, default=lambda: str(ObjectId()), editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()

class Workout(models.Model):
    _id = models.CharField(max_length=24, primary_key=True, default=lambda: str(ObjectId()), editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
