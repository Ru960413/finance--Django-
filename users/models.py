from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

# To-Do: implement user profile model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, null=True, blank=True)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    username = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    bankAccount = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

