from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def usersignup(request):
    return render(request,'usersignup.html')