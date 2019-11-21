from django import forms


class MyForm(forms.Form):
    content = forms.CharField(required=True)