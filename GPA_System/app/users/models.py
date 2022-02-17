from pyexpat import model
from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=100, blank=False, null= False)
    last_name = models.CharField(max_length=100, blank=False, null= False)
    email = models.EmailField(max_length=60,blank=True, null= False)
    phone_number = models.CharField(max_length=12, blank=True)