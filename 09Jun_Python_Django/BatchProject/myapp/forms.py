from dataclasses import fields
from pyexpat import model
from django import forms
from .models import userSignup,mynotes

class signupForm(forms.ModelForm):
    class Meta:
        model=userSignup
        fields='__all__'


class notesForm(forms.ModelForm):
    class Meta:
        model=mynotes
        fields=['title','cate','selectfile','comments']
    