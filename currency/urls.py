from django.urls import path
from . import views



urlpatterns = [
    # path takes 3 parameters, first: the path, second: the function which will then trigger HttpResponse
    
    # setting project page to the default page
    path('',  views.currencyDashboard, name='currencyDashboard'),
    path('quote/', views.quote, name='quote'),
    path('buy/', views.buy, name="buy"),
    path('sell/', views.sell, name="sell"),
    path('history/', views.history, name="history"),
    #path('currencyOwn/', views.currencyOwn, name="currencyOwn"),
    
]