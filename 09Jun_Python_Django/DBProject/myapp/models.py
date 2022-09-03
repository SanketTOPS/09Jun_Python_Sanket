import email
from statistics import mode
from django.db import models

# Create your models here.

class signup_master(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=12)
    dob=models.DateField()
    mobile=models.BigIntegerField()
    address=models.TextField()

    def __str__(self):
        return self.firstname
