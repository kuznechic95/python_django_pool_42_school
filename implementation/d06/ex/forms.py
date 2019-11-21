from django import forms
from django.contrib.auth.models import User
from .models import Tip

class SignupForm(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput, initial='')
	verif_password = forms.CharField(required=True, widget=forms.PasswordInput, initial='')
	def clean(self):
		form_data = super(SignupForm, self).clean()
		u = User.objects.filter(username=form_data['username'])
		if len(u) > 0:
			self._errors['username'] = ["The name entered is already taken"]
		if form_data['password'] != form_data['verif_password']:
			self._errors['password'] = ["The password must be identical in the 2 password fields"]
		return form_data


class LoginForm(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput, initial='')


class TipForm(forms.ModelForm):
	class Meta:
		model = Tip
		fields = ['content']