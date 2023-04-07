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
def buy(request):
    pass



@login_required(login_url='login')
def quote(request):
    pass



@login_required(login_url='login')
def sell(request):
    pass



@login_required(login_url='login')
def history(request):
    pass