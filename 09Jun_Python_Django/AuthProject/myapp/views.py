from django.shortcuts import redirect, render
from django.urls import is_valid_path
from .forms import usersignupForm
from .models import userSignup
from django.contrib.auth import logout

# Create your views here.

def index(request):
    if request.method=='POST':
        unm=request.POST['username']
        pas=request.POST['password']
        user=userSignup.objects.filter(username=unm,password=pas)
        if user:
            print("Login Successfully!")
            request.session["user"]=unm
            return redirect('home')
        else:
            print("Error!Login Fail")
    return render(request,'index.html')

def usersignup(request):
    if request.method=='POST':
        newuser=usersignupForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            print("Your account has been created!")
            return redirect('home')
        else:
            print(newuser.errors)
    return render(request,'usersignup.html')

def home(request):
    user=request.session.get('user')
    return render(request,'home.html',{'user':user})

def userlogout(request):
    logout(request)
    return redirect("/")