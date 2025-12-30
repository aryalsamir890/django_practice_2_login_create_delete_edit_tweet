from django import forms
from .models import tweet
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class login(forms.ModelForm):
    class Meta:
        model=tweet
        fields=['bio','photo']


class create_user(UserCreationForm):
    class Meta:
        model=User
        fields=('username','password1','password2')

