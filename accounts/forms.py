from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.db.models import fields
from django.contrib.auth.models import User
from .models import profile


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
class ProfileForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['city','phone_number','image']
       