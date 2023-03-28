from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

# To-Do: implement user login, logout, register
# To-Do: put login and register form on the index page
def homePage(request):
    return render(request, "users/index.html")


def UserLogin(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]

        try:
            user = User.objects.get(username=username)
        except:
            pass

        user=authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/dashboard')
        else:
            pass

    return render(request, 'users/login.html')


# This function is not working...
def register(request):
    form = CustomUserCreationForm()
    
    if request.method == "POST":
        form=CustomUserCreationForm(request.POST)
        # print(form)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()

            login(request, user)

            return redirect('/dashboard')



    context = {'form':form}
    return render(request, 'users/register.html', context)



@login_required(login_url='login')
def UserLogout(request):

    logout(request)
    return render(request, "users/index.html")



@login_required(login_url='login')
def dashboard(request):
    return render(request, 'users/dashboard.html')
