from django.shortcuts import render
from .forms import CustomUserCreationForm

# Create your views here.

# To-Do: implement user login, logout, register
# To-Do: put login and register form on the index page
def homePage(request):
    return render(request, "users/index.html")


def UserLogin(request):
    context= {}
    return render(request, 'users/login.html', context)


def register(request):
    # form = CustomUserCreationForm()
    # context = {'form':form}
    context = {}
    return render(request, 'users/register.html', context)