from django.db import models

# Create your models here.
class Account(models.Model):
    name=models.CharField(max_length=32)
    DOB=models.DateField()
    Aadhar=models.BigIntegerField()
    pan=models.CharField(max_length=10)
    mobile=models.IntegerField()
    address=models.CharField(max_length=100)
    acc=models.BigAutoField( primary_key=True ,unique=True)
    balance=models.DecimalField(max_digits=7,decimal_places=2,default=1000.0)
    pin=models.IntegerField(default=0)
    email=models.EmailField(default='chinnasaikumar24@gmail.com')
    OTP=models.IntegerField(default=0)