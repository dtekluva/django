from django import forms
from django.contrib.auth.models import User

from useraccount.models import UserAccount

class UserAccountForm(forms.ModelForm):
    phone = forms.CharField(max_length=246)
    occupation = forms.CharField(max_length=13)
    class Meta:
        model = UserAccount
        fields = ('phone', 'occupation')

class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=256)
    first_name = forms.CharField(max_length=256)
    last_name = forms.CharField(max_length=256)
    email = forms.CharField(max_length=256)
    password = forms.CharField(max_length=256)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
