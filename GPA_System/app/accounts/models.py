from django.db import models
from app.users.models import Users

# Create your models here.
class Accounts(models.Model):
    # account id most be created with the first two letters of the user name 
    # +  first two letters of each last name of the user + current day(number)
    # +  current month(number)  +  current year(last 2 numbers)
    # exmaple: ezequiel vasquez campusano = ezvaca160221
    account_id = models.CharField(max_length=12, blank=False, null= False)
    account_number = models.CharField(max_length=12, blank=False, null= False)
    current_balance = models.FloatField(blank=False, null= False)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=False, null= False)
    