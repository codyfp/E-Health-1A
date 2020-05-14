from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


from System.forms import *
from System.models import *
from System.decorators import unauthenticated_user, allowed_users

import logging
# Log file configuration
logger = logging.getLogger('__name__')


def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


# Login view
@unauthenticated_user
def login_view(request, *args, **kwargs):
    form = LoginForm()
    logger.debug(request.user.is_authenticated)
    logger.debug(request.user.username)
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
            
            if user_profile.is_doctor:
                user_name = user.username
                return redirect('doctor_panel', user_name=user_name) # This is where I pass the dynamic url argument for doctor panel
            elif user_profile.is_patient:
                user_name = user.username
                return redirect('patient_panel', user_name=user_name) # This is where I pass the dynamic url argument for patient panel
            else: 
                logger.debug(user_profile.is_doctor)
                logger.debug(user_profile.is_patient)
                return redirect('home')
                
        else:
            messages.info(request, 'Username OR password is incorrect')
            logger.debug('User is not found')
        
    context = {'form':form}
    return render(request, 'login.html', context)


# Registration Views
@unauthenticated_user
def doctor_register_view(request):
    form = DoctorSignUpForm()
    
    if request.method == 'POST':
        form = DoctorSignUpForm(request.POST)
        
        
        if form.is_valid():
            user = form.save()
            doctor = UserProfile.objects.create(user=user)
            doctor.is_doctor = True
            doctor.organization = form.cleaned_data.get('organization')
            doctor.save()
            group, created = Group.objects.get_or_create(name='Doctors')
            user.groups.add(group)
            return redirect('login')
        else:
            logger.debug('Form is invalid')
            logger.debug(form.errors.as_data())
            

    context = {'form':form}
    return render(request, 'doctor_register.html', context)

@unauthenticated_user
def patient_register_view(request):
    form = PatientSignUpForm()
    
    
    if request.method == 'POST':
        form = PatientSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            patient = UserProfile.objects.create(user=user)
            patient.is_patient = True
            patient.save()
            group, created = Group.objects.get_or_create(name='Patients')
            user.groups.add(group)
            return redirect('login')
        else:
            logger.debug('Form is invalid')
            logger.debug(form.errors.as_data())

    context = {'form':form}

    return render(request, 'patient_register.html', context) 



# This is the basic doctor panel. 
# It currently just displayes which doctor is logged in.
@login_required(login_url='login')
@allowed_users(allowed_roles=['Doctors'])
def doctor_panel_view(request, user_name):
    doctor = request.user

    context = {'user':doctor}
    return render(request, 'doctor_panel.html', context)

# This is the basic patient panel. 
# It currently just displayes which patient is logged in.
@login_required(login_url='login')
@allowed_users(allowed_roles=['Patients'])
def patient_panel_view(request, user_name):
    patient = request.user

    context = {'user': patient}
    return render(request, 'patient_panel.html', context)

@login_required(login_url='login')
def appointment_view(request, user_name,*args, **kwargs):
    
    patient = User.objects.get(username=user_name)
    user_appointments = Consultation.objects.filter(patient=patient)
    form = ConsultationForm()
    remove_id = request.POST.get('remove_id')

    if request.method == 'POST':
        if remove_id != None:
            logger.debug(remove_id)
            appt = user_appointments.get(id=remove_id)
            appt.deactivate()
            appt.save()
        else:
            form = ConsultationForm(request.POST)
            if form.is_valid():
                doctor = User.objects.get(username=form.cleaned_data.get('doc_username'))
                Consultation.objects.create(patient=patient, doctor=doctor, 
                complaint=form.cleaned_data.get('complaint'), date=form.cleaned_data.get('date'),
                time=form.cleaned_data.get('time'))
            else:
                logger.debug(form.errors.as_data())

    context = {'user_appointments': user_appointments,
                'form':form,
                'remove_id':remove_id}
    return render(request, 'appointment.html', context)

@login_required(login_url='login')
def schedule_view(request, user_name,*args, **kwargs):
    user      = User.objects.get(username=user_name)
    is_doctor = UserProfile.objects.get(user=user).is_doctor
    if is_doctor:
        user_appointments = Consultation.objects.filter(doctor=user)
    else:
        user_appointments = Consultation.objects.filter(patient=user)

    context = {'user_appointments': user_appointments}
    return render(request, 'schedule.html', context)

def register_view(request, *args, **kwargs):
    return render(request, "register.html", {})
    
# test frontend page
def test_view(request):

    return render(request, 'test.html', {})
