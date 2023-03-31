from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Transaction
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
    # context={}

    return render(request, 'bank/bank.html', context)



@login_required(login_url='login')
def deposit(request):
    if request.method=="POST":
        action = "deposit"
        context = {"action": action}

        # get current user's profile and bank account
        user_profile = request.user.userprofile
        bankAccount=BankAccount.objects.get(owner=user_profile)

        # use post method to submit form for deposit
        amountOfDeposit = request.POST["deposit"]

        if int(amountOfDeposit):
            # update user's balance
            bankAccount.balance += int(amountOfDeposit)
            bankAccount.save()

            # insert data into transaction table
            new_record = Transaction(account_id=bankAccount, amount=int(amountOfDeposit))
            new_record.save()

            # redirect to successful page let the user know the action is successful
            return render(request, 'bank/success.html', context)
            
        else:
            return render(request, 'bank/fail.html', context)



@login_required(login_url='login')
def loan(request):
    pass



# @login_required(login_url='login')
# def transfer(request):
#     pass


def calculateMonthlyInterest():
    # 2.5% per month
    pass



def calculateAnnualInterest():
    # add up monthly interest 
    pass