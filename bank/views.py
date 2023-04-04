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
            new_record = Transaction(account_id=bankAccount, amount=deposit)
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
        context = {"action": action}

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
                new_record = Transaction(account_id=bankAccount, amount=amount)
                new_record.save()

                # redirect to successful page let the user know the action is successful
                return render(request, 'bank/success.html', context)
            
            else:
                return render(request, 'bank/fail.html', context)

        else:
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
            new_record = Transaction(account_id=bankAccount, amount=loan)
            new_record.save()

            # redirect to successful page let the user know the action is successful
            return render(request, 'bank/success.html', context)
            
        else:
            return render(request, 'bank/fail.html', context)
        
    return render(request, 'bank/bank.html')




# @login_required(login_url='login')
# def transfer(request):
#     pass


def calculateMonthlyInterest():
    # 2.5% per month
    pass



def calculateAnnualInterest():
    # add up monthly interest 
    pass