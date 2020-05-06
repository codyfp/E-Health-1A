from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django.contrib.auth.models import User
from django import forms
from django.db import transaction

class DoctorSignUpForm(UserCreationForm):
    
    organization = forms.CharField(label='Current Health Organization', max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder':'Health Organisation'
    }) )
    username = forms.CharField(label='username', max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder':'Username'
    }) )
    first_name = forms.CharField(label='first_name', max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder':'Given Name'
    }) )
    last_name= forms.CharField(label='last_name', max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder':'Family Name'
    }) )
    email = forms.EmailField(label='email', max_length=100, widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder':'Email Adress'
    }) )
    password1 = forms.CharField(label='password1', max_length=100, widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder':'Password'
    }) )
    password2 = forms.CharField(label='password2', max_length=100, widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder':'Password'
    }) )
    
    class Meta:
        model   = User
        fields  = ['username', 'first_name', 'last_name', 'email', 'organization' ,'password1', 'password2']


class PatientSignUpForm(UserCreationForm):
    
    username = forms.CharField(label='username', max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder':'Username'
    }) )
    first_name = forms.CharField(label='first_name', max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder':'Given Name'
    }) )
    last_name= forms.CharField(label='last_name', max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder':'Family Name'
    }) )
    email = forms.CharField(label='email', max_length=100, widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder':'Email address'
    }) )
    password1 = forms.CharField(label='password1', max_length=100, widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder':'Password'
    }) )
    password2 = forms.CharField(label='password2', max_length=100, widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder':'Repeat password'
    }) )
    
    
    class Meta:
        model   = User
        fields  = ['username', 'first_name', 'last_name', 'email' ,'password1', 'password2']


class LoginForm(forms.Form):
    user_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username', 'name':'user_name'}),label='User Login', max_length=100, label_suffix='')
    user_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password', 'name':'user_password'}), label="Password", label_suffix='')
    class Meta:
        fields = ['user_name', 'user_password']


class PasswordResetForm(PasswordResetForm):
    email = forms.EmailField(max_length=254,widget=forms.EmailInput(attrs={'class':'form-control', 'autocomplete': 'email', 'placeholder':'Email address'}), label_suffix='')

