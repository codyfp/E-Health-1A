from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db import transaction

from System.models import Doctor, Patient

class DoctorSignUpForm(UserCreationForm):
    organization = forms.CharField(label='Current Health Organization', max_length=100)
    class Meta:
        model   = User
        fields  = ['username', 'first_name', 'last_name', 'email', 'organization' ,'password1', 'password2']


class PatientSignUpForm(UserCreationForm):
    class Meta:
        model   = User
        fields  = ('username', 'first_name', 'last_name', 'email' ,'password1', 'password2', )