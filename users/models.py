from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

# To-Do: implement user profile model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key=True)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    username = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.username)




class BankAccount(models.Model):
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=False, blank=False)
    account_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    interest = models.DecimalField(default=0, max_digits=12, decimal_places=2)


    def __str__(self):
        return str(self.owner)

    

