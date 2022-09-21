from django.shortcuts import render
from .forms import signupForm
from .models import userSignup

# Create your views here.

def index(request):

    return render(request,'index.html')

def notes(request):
    return render(request,'notes.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def profile(request):
    return render(request,'profile.html')