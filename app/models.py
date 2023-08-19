from django.db import models
from django.contrib.auth.models import User
import re
from django.core.exceptions import ValidationError


# Create your models here.



class Profile(models.Model):
    username=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic=models.ImageField()
    mobile_no=models.CharField(max_length=10)
    pan_card=models.CharField(max_length=20)
    account_no=models.CharField(max_length=10,blank=True)
    balance=models.DecimalField(max_digits=10,decimal_places=2,default=1)
    
class History(models.Model):
    Sender=models.CharField(max_length=100,default='')
    Reciver=models.CharField(max_length=100,default='')
    Money=models.DecimalField(max_digits=5,decimal_places=2,default=0.00)

    