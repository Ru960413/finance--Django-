from django.shortcuts import render, redirect
from .models import Transaction
from users.models import BankAccount
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.db.models import Sum
from decimal import *
# Create your views here.

# To-Do: implement deposit money, loan, transfer money features

@login_required(login_url='login')
def bankDashboard(request):
    page="bank"
    # get current user's profile
    user_profile = request.user.userprofile
    bankAccount = BankAccount.objects.get(owner=user_profile)

    # get current user's balance
    balance=bankAccount.balance

    now = datetime.now()
    # get user's transaction record
    users_record = Transaction.objects.filter(account_id=bankAccount)

    # calculate interest
    created = bankAccount.created
    today = datetime.now()
    year = today.year - created.year

    if year < 1:
        year = 1
    else:
        year=year

    interest = int(balance)*0.025*year
    bankAccount.interest = interest
    balance += Decimal(interest)
    bankAccount.save()

    # calculate totalDeposit, totalWithdrawal, interest
    totalWithdrawal = Transaction.objects.filter(account_id=bankAccount, type="withdrawal").aggregate(Sum('amount'))
    totalDeposit = Transaction.objects.filter(account_id=bankAccount, type="deposit").aggregate(Sum('amount'))

    context={"page":page, "balance": balance, "now": now, "users_record": users_record, "totalWithdrawal": totalWithdrawal["amount__sum"], "totalDeposit": totalDeposit["amount__sum"], "interest": interest}

    return render(request, 'bank/bank.html', context)



@login_required(login_url='login')
def deposit(request):
    if request.method=="POST" and "deposit" in request.POST:
        action = "deposit"
        context = {"action": action}

        # get current user's profile and bank account
        user_profile = request.user.userprofile
        bankAccount=BankAccount.objects.get(owner=user_profile)
       
        # use post method to submit form for deposit
        amountOfDeposit = request.POST["deposit"]

        if int(amountOfDeposit):
            deposit=int(amountOfDeposit)
            # update user's balance
            bankAccount.balance += deposit
            bankAccount.save()

            # insert data into transaction table
            new_record = Transaction(account_id=bankAccount, amount=deposit, type="deposit")
            new_record.save()

            # redirect to successful page let the user know the action is successful
            return render(request, 'bank/success.html', context)
            
        else:
            return render(request, 'bank/fail.html', context)
        
    return render(request, 'bank/bank.html')


# Not working... SOLVED
@login_required(login_url='login')
def withdrawal(request):
    if request.method=="POST" and "withdrawal" in request.POST:
        action = "withdrawal"

        # get current user's profile and bank account
        user_profile = request.user.userprofile
        bankAccount=BankAccount.objects.get(owner=user_profile)

        
        # use post method to submit form for deposit
        amountOfWithdrawal = request.POST["withdrawal"]

        if int(amountOfWithdrawal):
            withdrawal=int(amountOfWithdrawal)

            if bankAccount.balance >= withdrawal:
                # update user's balance
                bankAccount.balance = bankAccount.balance-withdrawal
                bankAccount.save()
                
                # insert data into transaction table
                amount = -withdrawal
                new_record = Transaction(account_id=bankAccount, amount=amount, type="withdrawal")
                new_record.save()
                context = {"action": action}

                # redirect to successful page let the user know the action is successful
                return render(request, 'bank/success.html', context)
            
            else:
                message="You don't have enough money to withdraw."
                context = {"action": action, "message":message}
                return render(request, 'bank/fail.html', context)

        else:
            message=""
            context = {"action": action, "message":message}
            return render(request, 'bank/fail.html', context)
        
    return render(request, 'bank/bank.html') 



@login_required(login_url='login')
def loan(request):
    if request.method=="POST" and "loan" in request.POST:
        action = "loan"
        context = {"action": action}

        # get current user's profile and bank account
        user_profile = request.user.userprofile
        bankAccount=BankAccount.objects.get(owner=user_profile)
       
        # use post method to submit form for deposit
        amountOfLoan = request.POST["loan"]

        if int(amountOfLoan) and bankAccount.balance >= int(amountOfLoan)*0.3:
            loan=int(amountOfLoan)
            # update user's balance
            bankAccount.balance += loan
            bankAccount.save()

            # insert data into transaction table
            new_record = Transaction(account_id=bankAccount, amount=loan, type="deposit")
            new_record.save()

            # redirect to successful page let the user know the action is successful
            return render(request, 'bank/success.html', context)
            
        else:
            message="You don't have enough deposit to request for the loan."
            context = {"action": action, "message":message}
            return render(request, 'bank/fail.html', context)
        
    return render(request, 'bank/bank.html')




# @login_required(login_url='login')
# def transfer(request):
#     pass
