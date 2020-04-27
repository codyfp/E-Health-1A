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

def login_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')#change this line to handle checking with database and redirecting to correct url
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def register_view(request, *args, **kwargs):
    return render(request, "register.html", {})

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

