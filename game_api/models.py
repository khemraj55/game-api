from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField()
    
    def __str__(self):
        return self.username

class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game_id = models.CharField(max_length=255, primary_key=True)
    string = models.CharField(max_length=255)
    is_palindrome = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user