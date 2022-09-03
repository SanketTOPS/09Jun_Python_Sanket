from django.http import HttpResponse
from django.shortcuts import render
import random
# Create your views here.

def index(request):
    #return HttpResponse("This is Django Response!")
    num={'num':random.randint(1111,9999)}
    nm={'name':'Nirav'}
    return render(request,'index.html',num)
