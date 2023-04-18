from django.urls import path
from . import views


urlpatterns = [
    # path takes 3 parameters, first: the path, second: the function which will then trigger HttpResponse
    
    # setting project page to the default page
    path('',  views.homePage, name=''),
    # path('dashboard/',  views.usersDashboard, name='dashboard'),
    path('login/',  views.UserLogin, name='login'),
    path('logout/',  views.UserLogout, name='logout'),
    path('register/',  views.register, name='register'),
    path('profile/',  views.profile, name='profile'),
    path('delete_account/',  views.deleteAccount, name='delete-account'),
    path('edit_profile/',  views.editProfile, name='edit-profile'),
    path('change_password/',  views.changePassword, name='change-password'),

    # TODO: add reset password urls
    
]