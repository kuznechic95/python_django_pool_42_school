from django import forms

class UpdateForm(forms.Form):
    opening_crawl = forms.CharField(required=True)