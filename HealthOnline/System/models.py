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
        # if self.is_patient:
        #     return "patient"
        # elif self.is_doctor:
        #     return "doctor"
        # else:
        #     return "neither"
        return self.first_name + " " + self.last_name

class Certificate(models.Model):
    doctor          = models.ForeignKey(User, blank=False, null=False, on_delete=models.PROTECT)
    certificate     = models.FileField(upload_to=('user_'+str(id)+'/Certificate/'))
    
    def get_doctor(self):
        return self.doctor.username
    
    def __str__(self):
        return self.get_doctor() + "_medical_certificate"

class Prescription(models.Model):
    doctor          = models.ForeignKey(User, related_name='doctor_prescription', blank=False, null=False, on_delete=models.PROTECT)
    patient         = models.ForeignKey(User, related_name='patient_prescription', blank=False, null=False, on_delete=models.PROTECT)
    dateTime        = models.DateTimeField(null=False, blank=False)
    drugs           = models.CharField(max_length=400, null=True, blank=True)
    notes           = models.CharField(max_length=500, null=True, blank=True)
    
    def get_doctor(self):
        return self.doctor.username
    
    def get_patient(self):
        return self.patient.username

    def __str__(self):
        return str(self.get_doctor()) + "_" + str(self.get_patient()) + "_" + str(self.dateTime) + "_prescription"

class Consultation(models.Model):
    doctor      = models.ForeignKey(User, related_name='doctor_consultation', blank=False, null=False, on_delete=models.PROTECT)
    patient     = models.ForeignKey(User, related_name='patient_consultation', blank=False, null=False, on_delete=models.PROTECT)
    description = models.CharField(max_length=1000, null=True, blank=True)
    dateTime    = models.DateTimeField(null=False, blank=False)
    
    def get_doctor(self):
        return self.doctor.username
    
    def get_patient(self):
        return self.patient.username

    def __str__(self):
        return str(self.get_doctor()) + "_" + str(self.get_patient()) + "_" + str(self.dateTime)