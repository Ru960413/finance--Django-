from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model= User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

        labels = {
            'first_name': 'Name',
            'last_name': 'Last Name',
        }
