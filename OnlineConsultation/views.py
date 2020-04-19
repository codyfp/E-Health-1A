from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    return HttpResponse('Welcome to the Login Page')

def register(request):
    return HttpResponse('Register Page')

def patientHomePage(request): 
    return HttpResponse('Patient Home Page')
    
def doctorHomePage(request):
    return HttpResponse('Doctor Home Page')

def doctorPanel(request):
    return HttpResponse('Doctor Panel')