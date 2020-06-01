from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import logout
from django.utils import timezone
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
import datetime

from django.conf import settings

from System.forms import *
from System.models import *
from System.decorators import unauthenticated_user, allowed_users

import logging
# Log file configuration
logger = logging.getLogger('__name__')

@unauthenticated_user
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
                return redirect('admin')
                
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
            try:
                appt = user_appointments.get(id=remove_id)
                appt.deactivate()
                appt.save()
            except:
                messages.info(request, 'No consultation found. Please try again.')
        else:
            form = ConsultationForm(request.POST)
            if form.is_valid():
                try:
                    doctor = User.objects.get(username=form.cleaned_data.get('doc_username'))
                    Consultation.objects.create(patient=patient, doctor=doctor, 
                    complaint=form.cleaned_data.get('complaint'), date=form.cleaned_data.get('date'),
                    time=form.cleaned_data.get('time'))
                except User.DoesNotExist:
                    messages.info(request, 'No Doctor Found. Please try again.')

            else:
                logger.debug(form.errors.as_data())

    context = {'user_appointments': user_appointments,
                'form':form,
                'remove_id':remove_id}
    return render(request, 'appointment.html', context)

@login_required(login_url='login')
def schedule_view(request, user_name,*args, **kwargs):
    user      = User.objects.get(username=user_name)

    date = timezone.now().date()
    wk_day = date.weekday()
    date -= datetime.timedelta(days=wk_day)
    
    dates = []
    for i in range(0, 7):
        dates.append(date)
        date += datetime.timedelta(days=1)
    for dt in dates: logger.debug(dt)
    
    is_doctor = UserProfile.objects.get(user=user).is_doctor
    
    if is_doctor:
        monday = Consultation.objects.filter(doctor=user, date=dates[0], is_active=True)
        tuesday = Consultation.objects.filter(doctor=user, date=dates[1], is_active=True)
        wednesday = Consultation.objects.filter(doctor=user, date=dates[2], is_active=True)
        thursday = Consultation.objects.filter(doctor=user, date=dates[3], is_active=True)
        friday = Consultation.objects.filter(doctor=user, date=dates[4], is_active=True)
        saturday = Consultation.objects.filter(doctor=user, date=dates[5], is_active=True)
        sunday = Consultation.objects.filter(doctor=user, date=dates[6], is_active=True)

    else:
        monday = Consultation.objects.filter(patient=user, date=dates[0], is_active=True)
        tuesday = Consultation.objects.filter(patient=user, date=dates[1], is_active=True)
        wednesday = Consultation.objects.filter(patient=user, date=dates[2], is_active=True)
        thursday = Consultation.objects.filter(patient=user, date=dates[3], is_active=True)
        friday = Consultation.objects.filter(patient=user, date=dates[4], is_active=True)
        saturday = Consultation.objects.filter(patient=user, date=dates[5], is_active=True)
        sunday = Consultation.objects.filter(patient=user, date=dates[6], is_active=True)


    context = { 'monday': monday,
                'tuesday': tuesday,
                'wednesday': wednesday,
                'thursday' : thursday,
                'friday' : friday,
                'saturday' : saturday,
                'sunday' : sunday,
                }
    return render(request, 'scheduletest.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Patients', 'Doctor'])
def list_prescription_view(request, user_name):
    user = User.objects.get(username=user_name)
    user_profile = UserProfile.objects.get(user=user)
    
    if user_profile.is_doctor:
        prescriptions = Prescription.objects.filter(doctor=user)
    else:
        prescriptions = Prescription.objects.filter(patient=user)
    
    
    if request.method == 'POST':
        prescription = Prescription.objects.get(id=request.POST['prescription_id'])
        body = 'Your prescription by Dr. ' + prescription.doctor.first_name + " " + prescription.doctor.last_name
        email = EmailMessage(subject='Health Online Prescription',
                             body=body,  
                             to=[user.email])
        email.attach_file(settings.MEDIA_ROOT + str(prescription.prescription_file))
        email.send()
        messages.info(request, 'Email Sent')
    
    
    context = {'prescriptions': prescriptions,
                'is_doctor':user_profile.is_doctor}
    return render(request, 'patient_prescription.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Doctors'])
def create_prescription_view(request, user_name, *args, **kwargs):
    form = PrescriptionForm()
    doctor = User.objects.get(username=user_name)
    if request.method == 'POST':
        form = PrescriptionForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                patient = User.objects.get(username=form.cleaned_data.get('patient_username'))
                prescription = Prescription(doctor=doctor, patient=patient, dateTime=timezone.now(),
                medication=form.cleaned_data.get('medication'), 
                description=form.cleaned_data.get('description'),
                prescription_file=request.FILES['prescription_file'])
                prescription.save()
                return redirect('doctor_panel', user_name=user_name)
            except User.DoesNotExist:
                messages.info(request, 'No User Found. Please try again.')
        else:
            logger.debug(form.errors.as_data())

    context = {'form':form}
    return render(request, 'doctor_prescription.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Doctors'])
def doctor_profile_view(request, user_name):
    
    doctor = User.objects.get(username=user_name)
    doctor_profile = UserProfile.objects.get(user=doctor)

    form = DoctorProfileForm()
    location = None

    if request.method == 'POST':
        form = DoctorProfileForm(request.POST)
        
        if form.is_valid():
            replacement_email = form.cleaned_data.get('email')
            replacement_organization = form.cleaned_data.get('organization')
            location = form.cleaned_data.get('location')

            if replacement_email:
                doctor.email = replacement_email
                doctor.save()

            if replacement_organization:
                doctor_profile.organization = replacement_organization
                doctor_profile.save()

            if location:
                doctor_profile.location = location
                doctor_profile.save()

        else:
            logger.debug(form.errors.as_data())

    context = {'form' : form,
                'doctor_profile': doctor_profile,
                'location' : location,
            }
    return render(request, 'doctor_profile.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Patients'])
def patient_profile_view(request, user_name):
    
    patient = User.objects.get(username=user_name)
    patient_profile = UserProfile.objects.get(user=patient)

    form = PatientProfileForm()
    
    if request.method == 'POST':
        form = PatientProfileForm(request.POST)
        
        if form.is_valid():
            replacement_email = form.cleaned_data.get('email')
           
            if replacement_email:
                patient.email = replacement_email
                patient.save()

        else:
            logger.debug(form.errors.as_data())

    context = {'form' : form,
                'patient_profile': patient_profile,
            }
    return render(request, 'patient_profile.html', context)



def logout_view(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('home')
