# DONE To-Do: When user register create a bank account and the user's profile DONE
from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from .models import UserProfile, BankAccount
from django.dispatch import receiver


# create User Profile and user's bank account automatically after user is registered 
#@receiver(post_save, sender=User)
def create_Profile(sender, instance, created, **kwargs):
    if created:
        user = instance
        userprofile = UserProfile.objects.create(
            user=user,
            email=user.email,
            username=user.username,
            firstName = user.first_name,
            lastName=user.last_name,
        )
        print("User's profile is created")

        bankaccount= BankAccount.objects.create(
            owner=userprofile,
        )

# TODO: When user is deleted close bank account and delete user profile


post_save.connect(create_Profile, sender=User)

