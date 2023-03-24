from django.shortcuts import render
from django.http import HttpResponse
from .models import Transactions
from django.contrib.auth.decorators import login_required
# Create your views here.

# To-Do: implement deposit money, loan, transfer money features


def bankDashboard(request):
    render(request, 'bank/bank.html')


@login_required(login_url='login')
def deposit(request):
    pass


@login_required(login_url='login')
def loan(request):
    pass



@login_required(login_url='login')
def transfer(request):
    pass