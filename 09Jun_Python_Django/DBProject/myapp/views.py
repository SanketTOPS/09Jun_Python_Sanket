from urllib.request import Request
from django.shortcuts import render
from .forms import signupForm
from .models import signup_master

# Create your views here.

def index(request):
    if request.method=='POST':
        newuser=signupForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            print("Your account has been created!")
        else:
            print(newuser.errors)
    return render(request,'index.html')

def showdata(request):
    stdata=signup_master.objects.all()
    return render(request,'showdata.html',{'data':stdata})