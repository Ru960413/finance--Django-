from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.models import BankAccount
from .helpers import convert, twd, lookup
# Create your views here.


@login_required(login_url='login')
def currencyDashboard(request):
    page="currency"
    context={"page":page}
    return render(request, 'currency/currencyDashboard.html', context)



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
            
            context={"amount":amount, "result": twd(result), "from_currency":from_currency}
            return render(request, "currency/quoted.html", context)
        
    return render(request, 'currency/currencyDashboard.html') 



@login_required(login_url='login')
def buy(request):
    pass



@login_required(login_url='login')
def sell(request):
    pass



# access currencyTransaction table and then load the data dynamically to currencyDashboard
@login_required(login_url='login')
def history(request):
    pass



# access currencyTransaction table and then load the data dynamically to currencyDashboard
@login_required(login_url='login')
def currencyOwn(request):
    pass