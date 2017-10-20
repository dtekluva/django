from django import forms
from django.contrib.auth.models import

from useraccount.models import useraccount

class UserAccountForm(forms.ModelForm):
    phone       =forms.CharField(max_length=13)
    occupation  =forms.CharField(max_length=256)

    class Meta:
        model =UserAccount
        fields=('phone','occupation')
        