from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

# To-Do: implement user login, logout, register
# To-Do: put login and register form on the index page
def homePage(request):
    page="home"
    context={"page":page}
    return render(request, "users/index.html", context)


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
            return redirect('bankDashboard')
        else:
            pass

    return render(request, 'users/login.html')



# This function is not working...SOLVED(It's because the password entered isn't long enough lol)
def register(request):

    form = CustomUserCreationForm()
    if request.method == "POST":
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()

            messages.success(request, "Account was created successfully!" )
            
            login(request, user)
            return redirect('bankDashboard')
        
        else:
            messages.error(request, "An error has occurred...")


    context = {'form':form}
    return render(request, 'users/register.html', context)



@login_required(login_url='login')
def UserLogout(request):

    logout(request)
    messages.success(request, "User logged out successfully!" )
    return render(request, "users/index.html")



# @login_required(login_url='login')
# def dashboard(request):
#     return render(request, 'users/dashboard.html')
