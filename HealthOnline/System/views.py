from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

from System.forms import DoctorSignUpForm, PatientSignUpForm 
from System.models import UserProfile


import logging
# Log file configuration
logger = logging.getLogger('__name__')


# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def login_view(request, *args, **kwargs):
    return render(request, "login.html", {})

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
            username = form.cleaned_data.get('username')
            return redirect('home')
        else:
            logger.debug('Form is invalid')
            logger.debug(form.errors.as_data())
            

    context = {'form':form}
    return render(request, 'doctor_register.html', context)

def patient_register_view(request):
    form = PatientSignUpForm()

    if request.method == 'POST':
        form = PatientSignUpForm(request.POST)
        if form.is_valid:
            user = form.save()
            patient = UserProfile.objects.create(user=user)
            patient.is_patient = True

    context = {'form':form}

    return render(request, 'patient_register.html', context) #patient_register.html needs to be created and changed with this 

    return render(request, 'signup.html', context) #patient_register.html needs to be created and changed with this 

# test frontend page
def test_view(request):
    return render(request, "test.html", {})

