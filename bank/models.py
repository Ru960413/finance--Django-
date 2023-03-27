from django.db import models
from users.models import BankAccount
# Create your models here.

# To-Do : implement transaction model

class Transactions(models.Model):
    account_id = models.ForeignKey(BankAccount, on_delete=models.CASCADE, null=False, blank=False)
    time = models.DateTimeField(auto_now=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.account_id)