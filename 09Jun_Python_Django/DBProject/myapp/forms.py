from dataclasses import fields
from pyexpat import model
from django import forms
from .models import signup_master


class signupForm(forms.ModelForm):
    class Meta:
        model=signup_master
        fields='__all__'


class updateForm(forms.ModelForm):
    class Meta:
        model=signup_master
        fields=['firstname','lastname','email','mobile']