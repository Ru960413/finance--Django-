from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
from django.forms import ModelForm



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model= User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

        labels = {
            'first_name': 'Name',
            'last_name': 'Last Name',
        }



class UserProfileForm(ModelForm):
    class Meta:
        model=UserProfile
        fields = ['firstName', 'lastName', 'email', 'username', 'profile_image']
        labels = {
            'firstName': 'Name',
            'lastName': 'Last Name',
        }
