from django.urls import path
from . import views


urlpatterns = [
    # path takes 3 parameters, first: the path, second: the function which will then trigger HttpResponse
    path('',  views.bankDashboard, name='bankDashboard'),
    path('deposit/',  views.deposit, name='deposit'),
    path('withdrawal/',  views.withdrawal, name='withdrawal'),
    path('loan/',  views.loan, name='loan'),
]