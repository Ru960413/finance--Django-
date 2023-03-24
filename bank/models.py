from django.db import models
from users.models import Profile

# Create your models here.

# To-Do : implement transaction model

class Transactions(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    time = models.TimeField()
