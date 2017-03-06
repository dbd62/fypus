import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class LoginForm(forms.Form):
	email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label="Email address")
	password = forms.CharField(label=_("Password"), max_length=100, widget=forms.PasswordInput)

class RegistrationForm(forms.Form):
    first_name = forms.CharField(label=_("First Name"), max_length=100, widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    last_name = forms.CharField(label=_("Last Name"), max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    phone = forms.CharField(label=_("Phone"), max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Phone'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs=dict(required=True, max_length=30, placeholder="Email")), label=_("Email address"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False, placeholder="Password")), label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False, placeholder="Password")), label=_("Password (again)"))
 
    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists. Please try another one."))
 
    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
            return self.cleaned_data