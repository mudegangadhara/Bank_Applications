from django import forms
from app.models import *

class Userform(forms.ModelForm):
    class Meta:
        model=User
        fields=['username', 'password', 'email']
        help_texts={'username':' '}
        widgets={'password': forms.PasswordInput}

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['profile_pic','mobile_no','pan_card','balance']
        help_texts={'profile_pic':''}



        