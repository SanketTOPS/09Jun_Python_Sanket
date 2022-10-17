from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import userData


class userSerializers(serializers.ModelSerializer):
    class Meta:
        model=userData
        #fields='__all__'
        fields=['id','name','email','sub']