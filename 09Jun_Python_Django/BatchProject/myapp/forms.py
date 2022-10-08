from dataclasses import fields
from pyexpat import model
from django import forms
from .models import userSignup,mynotes,contact

class signupForm(forms.ModelForm):
    class Meta:
        model=userSignup
        fields='__all__'


class notesForm(forms.ModelForm):
    class Meta:
        model=mynotes
        fields=['title','cate','selectfile','comments']
    
class contctFrom(forms.ModelForm):
    class Meta:
        model=contact
        fields='__all__'

    