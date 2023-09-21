from django import forms
from balapp.models import Balance
from django.contrib.auth.models import User

class PayForm(forms.ModelForm):
    class Meta:
        model=Balance
        fields='__all__'

class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']
