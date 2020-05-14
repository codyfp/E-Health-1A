from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout

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

    return render(request, 'patient_register.html', context) 

# This is the basic doctor panel. 
# It currently just displayes which doctor is logged in.
def doctor_panel_view(request, user_name):
    doctor = request.user

    context = {'user':doctor}
    return render(request, 'doctor_panel.html', context)

# This is the basic patient panel. 
# It currently just displayes which patient is logged in.
def patient_panel_view(request, user_name):
    patient = request.user

    context = {'user': patient}
    return render(request, 'doctor_panel.html', context)

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
            user_profile = UserProfile.objects.get(user=user)
            # I added this statement to redirect user to doctor 
            # panel if it is a doctor and to patient panel if patient.
            if(user_profile.is_doctor == True):
                user_name = user.username
                return redirect('doctor_panel', user_name=user_name) # This is where I pass the dynamic url argument for doctor panel
            else:
                user_name = user.username
                return redirect('patient_panel', user_name=user_name) # This is where I pass the dynamic url argument for patient panel
        else:
            messages.info(request, 'Username OR password is incorrect')
            logger.debug('User is not found')

    context = {'form':form}
    return render(request, 'login.html', context)

# test frontend page
def test_view(request):

    return render(request, 'test.html', {})


def appointment_view(request, *args, **kwargs):
    
    return render(request, 'appointment.html', {})

def register_view(request, *args, **kwargs):
    return render(request, "register.html", {})

def logout_view(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('home')
