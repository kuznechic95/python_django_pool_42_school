from django import forms
from django.contrib import auth


class UserLoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)


class CreateTipForm(forms.Form):
    text = forms.CharField(required=True)
