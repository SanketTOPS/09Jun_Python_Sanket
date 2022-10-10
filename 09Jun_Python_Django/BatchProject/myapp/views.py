import imp
from django.shortcuts import redirect, render
from django.urls import is_valid_path
from .forms import signupForm,notesForm,contctFrom
from .models import userSignup
from django.contrib.auth import logout
from django.core.mail import send_mail
from BatchProject import settings
import random
import requests


# Create your views here.

def auth_signup(request):
    newuser=signupForm(request.POST)
    if newuser.is_valid():
        newuser.save()
        print("Your account has been created!")
        return redirect('notes')
    else:
        print(newuser.errors)

def auth_signin(request):
    unm=request.POST['username']
    pas=request.POST['password']
    user=userSignup.objects.filter(username=unm,password=pas)
    if user:
        print("Login Successfully!")
        request.session['user']=unm
        return redirect('notes')
    else:
        print("Error....Login falid!")


def index(request):
    if request.method=='POST':
        if request.POST.get('signup')=='signup':
            #auth_signup(request)
            newuser=signupForm(request.POST)
            if newuser.is_valid():
                newuser.save()
                print("Your account has been created!")

                # Email Sending Code
                #send_mail('Welcome!',f"Hello User!\nYour account has been created with us!\nEnjoy our services.\n\nThank & Regarards!\n+91 97247 99469 | sanket@tops-int.com",settings.EMAIL_HOST_USER,['sanganiraj999@gmail.com','deephansaliya96@gmail.com','mayurvadher59@gmail.com','rajdeepsinhchavda890@gmail.com','maishrilimbasiya@gmail.com'])
                otp=random.randint(1111,9999)
                sub='Welcome!'
                msg=f"Hello User!\nYour account has been created with us!\nEnjoy our services.\nYour One Time Password is {otp}\n\nThank & Regarards!\n+91 97247 99469 | sanket@tops-int.com"
                from_ID=settings.EMAIL_HOST_USER
                to_ID=[request.POST['username']]
                send_mail(sub,msg,from_ID,to_ID)
                return redirect('notes')
            else:
                print(newuser.errors)
        elif request.POST.get('login')=='login':
            #auth_signin(request)
            unm=request.POST['username']
            pas=request.POST['password']
            user=userSignup.objects.filter(username=unm,password=pas)
            if user:
                print("Login Successfully!")
                request.session['user']=unm

                # Send SMS Code
                otp=random.randint(1111,9999)
                url = "https://www.fast2sms.com/dev/bulkV2"

                payload = f"variables_values={otp}&route=otp&numbers=7698147545,8128117107,7600076171,8799126961,9427630925"
                headers = {
                    'authorization': "PSqGhvu5BkQv1WEvvWH6PIgV0vr1IcOIEzgsN1fZMHFG0WJapJ1hGGIwYfq8",
                    'Content-Type': "application/x-www-form-urlencoded",
                    'Cache-Control': "no-cache",
                    }

                response = requests.request("POST", url, data=payload, headers=headers)

                print(response.text)
                return redirect('notes')
            else:
                print("Error....Login falid!")
    return render(request,'index.html')

def notes(request):
    user=request.session.get('user')
    if request.method=='POST':
        note=notesForm(request.POST,request.FILES )
        if note.is_valid():
            note.save()
            print("Your notes has been uploaded!")
        else:
            print(note.errors)
    return render(request,'notes.html',{'user':user})

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method=='POST':
        newcont=contctFrom(request.POST)
        if newcont.is_valid():
            newcont.save()
            print("Your feedback has been sent.")
        else:
            print(newcont.errors)
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