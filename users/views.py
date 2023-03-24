from django.shortcuts import render
from .forms import CustomUserCreationForm

# Create your views here.

# To-Do: implement user login, logout, register
def homePage(request):
    context= {}
    return render(request, "users/index.html", context)


def UserLogin(request):
    context= {}
    return render(request, 'users/login.html', context)


def register(request):
    # form = CustomUserCreationForm()
    # context = {'form':form}
    context = {}
    return render(request, 'users/register.html', context)