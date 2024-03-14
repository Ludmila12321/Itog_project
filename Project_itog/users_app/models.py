from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    registration_date = models.DateField(auto_now_add=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.username}, {self.email}'

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)