from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User

from System.forms import DoctorSignUpForm, PatientSignUpForm 
from System.models import Doctor, Patient


import logging
# Log file configuration
logger = logging.getLogger('__name__')


# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def register_view(request, *args, **kwargs):
    return render(request, "register.html", {})

def DoctorSignUpView(request):
    form = DoctorSignUpForm()
    
    if request.method == 'POST':
        form = DoctorSignUpForm(request.POST)
        logger.debug(form)
        if form.is_valid():
            user = form.save()
            doctor = Doctor.objects.create(user=user)
            doctor.organization.add(form.cleaned_data.get('organization'))
        else:
            logger.debug('Form is invalid')
            logger.debug(form.errors.as_data())
            

    context = {'form':form}
    return render(request, 'doctor_register.html', context)

def PatientSignUpView(request):
    form = PatientSignUpForm()

    if request.method == 'POST':
        form = PatientSignUpForm(request.POST)
        if form.is_valid:
            user = form.save()
            patient = Patient.objects.create(user=user)
    
    context = {'form':form}
    return render(request, 'signup.html', context) #patient_register.html needs to be created and changed with this 
