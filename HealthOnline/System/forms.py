from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db import transaction

class DoctorSignUpForm(UserCreationForm):
    organization = forms.CharField(label='Current Health Organization', max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }) )
    username = forms.CharField(label='Current Health Organization', max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }) )
    first_name = forms.CharField(label='Current Health Organization', max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }) )
    last_name= forms.CharField(label='Current Health Organization', max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }) )
    email = forms.CharField(label='Current Health Organization', max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }) )
    password1 = forms.CharField(label='Current Health Organization', max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }) )
    password2 = forms.CharField(label='Current Health Organization', max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }) )
  
    class Meta:
        model   = User
        fields  = ['username', 'first_name', 'last_name', 'email', 'organization' ,'password1', 'password2']


class PatientSignUpForm(UserCreationForm):
    
    username = forms.CharField(label='Current Health Organization', max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }) )
    first_name = forms.CharField(label='Current Health Organization', max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }) )
    last_name= forms.CharField(label='Current Health Organization', max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }) )
    email = forms.CharField(label='Current Health Organization', max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }) )
    password1 = forms.CharField(label='Current Health Organization', max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }) )
    password2 = forms.CharField(label='Current Health Organization', max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }) )
    
    
    class Meta:
        
        
        model   = User
        fields  = ('username', 'first_name', 'last_name', 'email' ,'password1', 'password2', )