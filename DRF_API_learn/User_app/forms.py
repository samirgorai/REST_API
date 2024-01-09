from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class Create_user_form(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email']


class Login_form(forms.Form):
    username=forms.CharField(max_length=10)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
