from django.contrib import admin
from .models import UserProfile, BankAccount

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(BankAccount)