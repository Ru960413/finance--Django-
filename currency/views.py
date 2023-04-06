from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.models import BankAccount
import requests
# Create your views here.


@login_required(login_url='login')
def currencyDashboard(request):
    page="currency"
    context={"page":page}
    return render(request, 'currency/currencyDashboard.html', context)


# THis is not working... 
def api(request):
    # interact with exchange rate currency api

    url = 'https://v6.exchangerate-api.com/v6/de854dd1ac96a4c45b041347/latest/TWD'

    response = requests.get(url)
    data = response.json()

    return render(request, 'currency/currencyDashboard.html', {"data": data["conversion_rates"]["HKD"]})



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