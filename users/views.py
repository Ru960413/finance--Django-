from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, UserProfileForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile, BankAccount
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.

# To-Do: implement user login, logout, register: DONE
# To-Do: put login and register form on the index page


# If user is logged in then render profile page, otherwise render homepage
def profile(request):
    page = "profile"
    user_info = request.user.userprofile
    bankAccount = BankAccount.objects.get(owner=user_info)
    totalBalance = bankAccount.balance + bankAccount.interest
    context = {
        "page": page,
        "user_info": user_info,
        "bankAccount": bankAccount,
        "totalBalance": totalBalance,
    }
    return render(request, "users/profile.html", context)


def homePage(request):
    page = "home"
    context = {"page": page}
    return render(request, "users/index.html", context)


def UserLogin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            user = User.objects.get(username=username)
        except:
            pass

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Hello {user.first_name}! Welcome back!")
            return redirect("bankDashboard")
        else:
            pass

    return render(request, "users/login.html")


# This function is not working...SOLVED(It's because the password entered isn't long enough lol)
def register(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, "Account was created successfully!")

            login(request, user)
            return redirect("bankDashboard")

        else:
            messages.error(request, "An error has occurred...")

    context = {"form": form}
    return render(request, "users/register.html", context)


@login_required(login_url="login")
def UserLogout(request):
    logout(request)
    messages.success(request, "You've successfully logged out !")
    return redirect("")


@login_required(login_url="login")
def editProfile(request):
    profile = request.user.userprofile
    form = UserProfileForm(instance=profile)

    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profile")

    context = {"form": form}
    return render(request, "users/profile_form.html", context)


@login_required(login_url="login")
def inactivateAccount(request):
    if request.method == "POST":
        user_profile = request.user.userprofile
        User.objects.filter(username=user_profile.username).update(is_active=False)
        logout(request)
        return render(request, "users/success.html")

    return render(request, "users/inactivate_form.html")


@login_required(login_url="login")
def changePassword(request):
    form = PasswordChangeForm(user=request.user)

    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("profile")

    context = {"form": form}
    return render(request, "users/changePassword.html", context)
