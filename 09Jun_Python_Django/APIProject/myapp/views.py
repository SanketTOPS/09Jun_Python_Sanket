from django.shortcuts import render
from .models import userData
from .serializers import userSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

def index(request):
    return render(request,'index.html')


@api_view(['GET'])
def getall(request):
    if request.method=='GET':
        alluser=userData.objects.all()
        userserail=userSerializers(alluser,many=True)
        return Response(userserail.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getstid(request,id):
    if request.method=="GET":
        try:
            alluser=userData.objects.get(id=id)
            userserail=userSerializers(alluser)
        except userData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(userserail.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)
    





