from urllib.request import Request
from django.shortcuts import redirect, render
from .forms import signupForm,updateForm
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

def updatedata(request,sid):
    stid=signup_master.objects.get(id=sid)
    #print("Student ID:",stid)
    if request.method=='POST':
        updateform=signupForm(request.POST)
        if updateform.is_valid():
            updateform=signupForm(request.POST,instance=stid)
            updateform.save()
            print("Your data has been updated!")
            return redirect('showdata')
        else:
            print(updateform.errors)
    return render(request,'updatedata.html',{'stid':signup_master.objects.get(id=sid)})

def deletedata(request,sid):
    stid=signup_master.objects.get(id=sid)
    signup_master.delete(stid)
    return redirect('showdata')