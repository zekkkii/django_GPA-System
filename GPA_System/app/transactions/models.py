from django.db import models
from app.accounts.models import Accounts

# Create your models here.
class Transactions(models.Model):
    date = models.DateTimeField(auto_created=True, blank=False, null= False)
    transaction_type = models.CharField(max_length=6, blank=False, null= False)
    note = models.CharField(max_length=250, blank=True, )
    amount = models.FloatField(blank=False, null= False)
    account_id = models.ForeignKey(Accounts, on_delete=models.CASCADE, blank=False, null= False)
