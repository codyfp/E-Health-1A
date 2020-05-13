from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from django.contrib import messages

from django.http import HttpResponseRedirect


from System.forms import *
from System.models import UserProfile


import logging
# Log file configuration
logger = logging.getLogger('__name__')


# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def chat_view(request, *args, **kwargs):
    return render(request, "chat.html", {})

def login_view(request, *args, **kwargs):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('user_name')
            password = form.cleaned_data.get('user_password')
            user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
            logger.debug('User is not created')

    context = {'form':form}
    return render(request, 'login.html', context)


def doctor_register_view(request):
    form = DoctorSignUpForm()
    
    if request.method == 'POST':
        form = DoctorSignUpForm(request.POST)
        logger.debug(form)
        
        if form.is_valid():
            user = form.save()
            doctor = UserProfile.objects.create(user=user)
            doctor.is_doctor = True
            doctor.organization = form.cleaned_data.get('organization')
            return redirect('home')
        else:
            logger.debug('Form is invalid')
            logger.debug(form.errors.as_data())
            

    context = {'form':form}
    return render(request, 'doctor_register.html', context)

def patient_register_view(request):
    form = PatientSignUpForm()
    logger.debug(form)
    
    if request.method == 'POST':
        form = PatientSignUpForm(request.POST)
        if form.is_valid:
            user = form.save()
            patient = UserProfile.objects.create(user=user)
            patient.is_patient = True
            return redirect('home')
        else:
            logger.debug('Form is invalid')
            logger.debug(form.errors.as_data())

    context = {'form':form}

    return render(request, 'patient_register.html', context) #patient_register.html needs to be created and changed with this 


# test frontend page
def test_view(request):

    return render(request, 'test.html', {})


def register_view(request, *args, **kwargs):
    return render(request, "register.html", {})