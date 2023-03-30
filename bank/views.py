from django.shortcuts import render
from django.http import HttpResponse
from .models import Transactions
from users.models import BankAccount
from django.contrib.auth.decorators import login_required
# Create your views here.

# To-Do: implement deposit money, loan, transfer money features

@login_required(login_url='login')
def bankDashboard(request):
    
    # get current user's profile
    user_profile = request.user.userprofile
    bankAccount = BankAccount.objects.get(owner=user_profile)

    # get current user's balance
    balance=bankAccount.balance

    # get user's transaction record

    # calculate totalDeposit, totalWithdrawal, interest

    context={"balance": balance}

    return render(request, 'bank/bank.html', context)



@login_required(login_url='login')
def deposit(request):
    # if request.method=="POST":
    #     #get current user's profile
    #     user_profile = request.user.userprofile
    #     bankAccount = BankAccount.objects.get(owner=user_profile)

    #     #get current user's balance
    #     balance=bankAccount.balance
    #     # use post method to submit form to add money
    #     amountOfDeposit = request.POST["deposit"]

    #     balance += amountOfDeposit
    #     # insert data into transaction table

    #     # flash the message to let the user know the action is successful

    # # redirect the user to the bank dashboard
    # context={"balance": balance}

    context={}

    return render(request, 'bank/bank.html', context)



@login_required(login_url='login')
def loan(request):
    pass



@login_required(login_url='login')
def transfer(request):
    pass



def calculateMonthlyInterest():
        # 2.5% per month
        pass



def calculateAnnualInterest():
    # add up monthly interest 
    pass