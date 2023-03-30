from django.urls import path
from . import views


urlpatterns = [
    # path takes 3 parameters, first: the path, second: the function which will then trigger HttpResponse
    
    # setting project page to the default page
    path('',  views.homePage, name=''),
    path('login/',  views.UserLogin, name='login'),
    path('logout/',  views.UserLogout, name='logout'),
    path('register/',  views.register, name='register'),
    #path('dashboard/', views.dashboard, name='dashboard'),
    
]