from django.contrib.auth.models import User
from django.db import models


# Create your models here.

import logging
# Log file configuration
logger = logging.getLogger('__name__')

class Gender(models.Model):
    name = models.CharField(max_length=12, null=True, blank=True)

    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    code = models.CharField(max_length=3, null=True, blank=True)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Countries"

class UserProfile(models.Model):
    user                = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, default=0) 
    organization        = models.CharField(max_length=150, null=True, blank=True, default='')
    gender              = models.ForeignKey(Gender, blank=True, null=True, on_delete=models.PROTECT)
    birth_date          = models.DateField(blank=True, null=True)
    street              = models.CharField(max_length=150, null=True, blank=True)
    suburb              = models.CharField(max_length=50, null=True, blank=True)
    state               = models.ForeignKey(State, blank=True, null=True, on_delete=models.PROTECT)
    postal_code         = models.CharField(max_length=20, null=True, blank=True)
    country             = models.ForeignKey(Country, blank=True, null=True, on_delete=models.PROTECT)
    mobile_phone        = models.CharField(max_length=50, null=True, blank=True)
    created_date        = models.DateTimeField(null=True, blank=True)
    last_update         = models.DateTimeField(null=True, blank=True)
    Identity_Document   = models.FileField(upload_to=('user_'+str(id)+'/Identity/'))
    
    is_doctor           = models.BooleanField(default=False)
    is_patient          = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username + "_profile"

class Certificate(models.Model):
    doctor          = models.ForeignKey(User, blank=False, null=False, on_delete=models.PROTECT)
    certificate     = models.FileField(upload_to=('user_'+str(doctor)+'/Certificate/'))
    
    def get_doctor(self):
        return self.doctor.username
    
    def __str__(self):
        return self.get_doctor() + "_medical_certificate"

class Prescription(models.Model):
    doctor            = models.ForeignKey(User, related_name='doctor_prescription', blank=False, null=False, on_delete=models.PROTECT)
    patient           = models.ForeignKey(User, related_name='patient_prescription', blank=False, null=False, on_delete=models.PROTECT)
    dateTime          = models.DateTimeField(null=True, blank=True)
    medication        = models.CharField(max_length=400, null=True, blank=True)
    description       = models.CharField(max_length=500, null=True, blank=True)
    prescription_file = models.FileField(upload_to='prescriptions/', null=True)
    
    def get_doctor(self):
        return self.doctor.username
    
    def get_patient(self):
        return self.patient.username

    def __str__(self):
        return str(self.get_doctor()) + "_" + str(self.get_patient()) + "_" + str(self.dateTime) + "_prescription"

class Consultation(models.Model):
    doctor      = models.ForeignKey(User, related_name='doctor_consultation', blank=False, null=False, on_delete=models.PROTECT)
    patient     = models.ForeignKey(User, related_name='patient_consultation', blank=False, null=False, on_delete=models.PROTECT)
    complaint   = models.CharField(max_length=100, null=True, blank=True)
    date        = models.DateField(null=False, blank=False) 
    time        = models.TimeField(null=False, blank=False)
    is_active   = models.BooleanField(default=True)
    is_complete = models.BooleanField(default=False)

    def deactivate(self):
        self.is_active = False

    def mark_complete(self):
        self.is_complete = True
    
    def get_doctor(self):
        return self.doctor.username
    
    def get_patient(self):
        return self.patient.username

    def __str__(self):
        return str(self.get_doctor()) + "_" + str(self.get_patient()) + "_" + str(self.date) + "_" +str(self.time)
    