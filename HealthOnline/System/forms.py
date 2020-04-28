from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db import transaction

class DoctorSignUpForm(UserCreationForm):
    organisation = forms.CharField(label='Current Health Organisation', max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder':'Health Organisation'
    }) )
    username = forms.CharField(label='Current Health Organisation', max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder':'Username'
    }) )
    first_name = forms.CharField(label='Current Health Organisation', max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder':'Given Name'
    }) )
    last_name= forms.CharField(label='Current Health Organisation', max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder':'Family Name'
    }) )
    email = forms.CharField(label='Current Health Organisation', max_length=100, widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder':'Email Adress'
    }) )
    password1 = forms.CharField(label='Current Health Organisation', max_length=100, widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder':'Password'
    }) )
    password2 = forms.CharField(label='Current Health Organisation', max_length=100, widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder':'Password'
    }) )
  
    class Meta:
        model   = User
        fields  = ['username', 'first_name', 'last_name', 'email', 'organisation' ,'password1', 'password2']


class PatientSignUpForm(UserCreationForm):
    
    username = forms.CharField(label='Current Health Organisation', max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder':'Username'
    }) )
    first_name = forms.CharField(label='Current Health Organisation', max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder':'Given Name'
    }) )
    last_name= forms.CharField(label='Current Health Organisation', max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder':'Family Name'
    }) )
    email = forms.CharField(label='Current Health Organisation', max_length=100, widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder':'Email address'
    }) )
    password1 = forms.CharField(label='Current Health Organisation', max_length=100, widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder':'Password'
    }) )
    password2 = forms.CharField(label='Current Health Organisation', max_length=100, widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder':'Repeat password'
    }) )
    
    
    class Meta:
        
        
        model   = User
        fields  = ('username', 'first_name', 'last_name', 'email' ,'password1', 'password2', )


class LoginForm(forms.Form):
    user_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}),label='User Login', max_length=100, label_suffix='')
    user_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}), label="Password", label_suffix='')
