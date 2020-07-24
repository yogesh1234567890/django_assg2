from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class Form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model =login
        fields=['email','password']

class CreateUserForm(UserCreationForm):
    class Meta:
        model=get_user_model()
        fields=['username','email','password1','password2']