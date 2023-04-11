from django.db import models
from users.models import BankAccount
# Create your models here.

class currencyTransaction(models.Model):
    account_id = models.ForeignKey(BankAccount, on_delete=models.CASCADE, null=False, blank=False)
    time = models.DateTimeField(auto_now=True)
    currency = models.CharField(max_length=20, null=False, blank=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=10, null=True)


    def __str__(self):
        return str(self.amount)