from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import datetime

# Create your models here.


# TODO: add profile picture column
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    username = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    profile_image = models.ImageField(
        null=True,
        blank=True,
        upload_to="profiles/",
        default="profiles/user-default.png",
    )

    def __str__(self):
        return str(self.username)

    @property
    def imageURL(self):
        try:
            url = self.profile_image.url
        except:
            url = '/img/user-default.png'

        return url



class BankAccount(models.Model):
    owner = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, null=False, blank=False
    )
    account_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    interest = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    created = models.DateField(blank=True, default=datetime.now)

    def __str__(self):
        return str(self.owner)
