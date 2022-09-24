from django.shortcuts import redirect, render
from django.urls import is_valid_path
from .forms import signupForm
from .models import userSignup
from django.contrib.auth import logout

# Create your views here.

def index(request):
    if request.method=='POST':
        if request.POST.get('signup')=='signup':
            newuser=signupForm(request.POST)
            if newuser.is_valid():
                newuser.save()
                print("Your account has been created!")
                return redirect('notes')
            else:
                print(newuser.errors)
        elif request.POST.get('login')=='login':

            unm=request.POST['username']
            pas=request.POST['password']

            user=userSignup.objects.filter(username=unm,password=pas)
            if user:
                print("Login Successfully!")
                request.session['user']=unm
                return redirect('notes')
            else:
                print("Error....Login falid!")
    return render(request,'index.html')

def notes(request):
    user=request.session.get('user')
    return render(request,'notes.html',{'user':user})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def profile(request):
    user=request.session.get('user')
    cuser=userSignup.objects.get(username=user)
    if request.method=='POST':
        updateuser=signupForm(request.POST)
        if updateuser.is_valid():
            updateuser=signupForm(request.POST,instance=cuser)
            updateuser.save()
            print("Your profile has been updated!")
            return redirect('profile')
        else:
            print(updateuser.errors)
    return render(request,'profile.html',{'user':user, 'cuser':userSignup.objects.get(username=user)})

def userlogout(request):
    logout(request)
    return redirect("/")