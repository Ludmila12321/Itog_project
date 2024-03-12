from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    registration_date = models.DateField(auto_now_add=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}, {self.email}'