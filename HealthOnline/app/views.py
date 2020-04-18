from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def login(request):
    return HttpResponse('Login Page')
def register(request):
    return HttpResponse('Register Page')
def patientHomePage(request):  
    return HttpResponse('Patient Homepage')
def doctorHomePage(request):
    return HttpResponse('Doctor Homepage')
def doctorPanel(request):
    return HttpResponse('Doctor Panel')