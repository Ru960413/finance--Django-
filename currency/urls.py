from django.urls import path
from . import views



urlpatterns = [
    # path takes 3 parameters, first: the path, second: the function which will then trigger HttpResponse
    
    # setting project page to the default page
    path('',  views.currencyDashboard, name='currencyDashboard'),
    #path('api/', views.api, name='api'),
    
]