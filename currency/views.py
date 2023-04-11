from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import currencyTransaction
from users.models import BankAccount
from .helpers import twd, lookup
from decimal import *
from django.db.models import Sum, Count
# Create your views here.


@login_required(login_url='login')
def currencyDashboard(request):
    page="currency"
    context={"page":page}
    return render(request, 'currency/currencyDashboard.html', context)


# DONE
@login_required(login_url='login')
def quote(request):
    if request.method=="POST":
        action="quote"
        from_currency=request.POST["from_currency"]
        amount=request.POST["amount"]

        result=lookup(from_currency, amount)
        if from_currency==None:
            message="Please enter the currency code you want to quote"
            context={"action": action, "message": message}
            return render(request, "currency/fail.html", context)
        
        elif result==None:
            message="The currency that you are looking for doesn't exist"
            context={"action": action, "message": message}
            return render(request, "currency/fail.html", context)
        
        else:
            
            context={"amount":amount, "result": result, "from_currency":from_currency}
            return render(request, "currency/quoted.html", context)
        
    return render(request, 'currency/currencyDashboard.html') 



@login_required(login_url='login')
def buy(request):
    if request.method=="POST":
        # get user's profile and bank account
        user_profile = request.user.userprofile
        bankAccount = BankAccount.objects.get(owner=user_profile)

        # get the currency exchange result for which the user wants to buy
        action="buy"
        currency_code=request.POST["currency_code"]
        amount=request.POST["amount"]

        # see if user can afford it:
        # get user's bank account balance 
        balance = bankAccount.balance

        # check if there're values in the form
        if amount == None:
            message="Please enter the amount you want to buy."
            context={"action": action, "message": message}
            return render(request, 'currency/fail.html', context)
        
        elif currency_code == None:
            message="Please enter the currency you want to buy."
            context={"action": action, "message": message}
            return render(request, 'currency/fail.html', context)
        
        else:
            # get exchange result and compare it with user's balance to see if user can afford it
            result = lookup(currency_code, amount)
            result = Decimal(twd(result))

            # if user cannot afford it, render error message
            if result > balance:
                message="Sorry you cannot afford it..."
                context={"action": action, "message": message}
                return render(request, 'currency/fail.html', context)

            else:
                # update user's bank account
                bankAccount.balance -= result
                bankAccount.save()
            
                # add it to currency transaction record
                new_record = currencyTransaction(account_id=bankAccount, currency=currency_code, amount=amount, type="buy")
                new_record.save()

                context={"action": action}
                return render(request, 'currency/success.html', context)

    return render(request, 'currency/currencyDashboard.html')


# DONE
@login_required(login_url='login')
def sell(request):
    if request.method=="POST":
        # get user's profile and bank account
        user_profile = request.user.userprofile
        bankAccount = BankAccount.objects.get(owner=user_profile)

        # get the currency exchange result for which the user wants to buy
        action="sell"
        currency_code=request.POST["currency_code"]
        amount=request.POST["amount"]
        amount=int(amount)

        # check if there're values in the form
        if amount == None:
            message="Please enter the amount you want to exchange for."
            context={"action": action, "message": message}
            return render(request, 'currency/fail.html', context)
        
        elif currency_code == None:
            message="Please enter the currency you want to exchange for."
            context={"action": action, "message": message}
            return render(request, 'currency/fail.html', context)
        
        # check if user has enough to sell
        else:
            # get user's currency transaction record of the currency
            currency_own = currencyTransaction.objects.filter(account_id=bankAccount, currency= currency_code).aggregate(Sum('amount'))

            currency_own = int(currency_own["amount__sum"])
            
            # compare the amount of currency in the form to the amount of currency the user own:
            # if user doesn't have enough to sell, then render error message
            if amount > currency_own:
                message="Sorry, you don't have enough to sell..."
                context={"action": action, "message": message}
                return render(request, 'currency/fail.html', context)

            # else sell the currency and update user's back account balance
            else:
                # update user's bank account
                conversion=lookup(currency_code, amount)
                bankAccount.balance += Decimal(conversion)
                bankAccount.save()

                # add it into currency Transaction table
                amount=-amount
                new_record = currencyTransaction(account_id=bankAccount, currency=currency_code, amount=amount, type="sell")
                new_record.save()
                context={"action": action}

                return render(request, 'currency/success.html', context)
            
    return render(request, 'currency/currencyDashboard.html')



# access currencyTransaction table and then load the data dynamically to currencyDashboard
@login_required(login_url='login')
def history(request):
    # get user's profile and bank account
    user_profile = request.user.userprofile
    bankAccount = BankAccount.objects.get(owner=user_profile)
    users_record = currencyTransaction.objects.filter(account_id=bankAccount)
    context={"users_record": users_record}

    return render(request, 'currency/currencyDashboard.html', context)



# access currencyTransaction table and then load the data dynamically to currencyDashboard
# @login_required(login_url='login')
# def currencyOwn(request):
#     user_profile = request.user.userprofile
#     bankAccount = BankAccount.objects.get(owner=user_profile)
    
#     # get the sum of each currency from user's currencyTransaction table
#     currencies_own = currencyTransaction.objects.filter(account_id=bankAccount).values('currency').aggregate(Sum('amount')).order_by()

#     context={"currencies_own": currencies_own}

#     return render(request, 'currency/currencyDashboard.html', context)