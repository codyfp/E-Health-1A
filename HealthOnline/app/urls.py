from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('login/', views.login),
    path('register/', views.register),
    path('patienthomepage', views.patientHomePage),
    path('doctorhomepage', views.doctorHomePage),
    path('doctorpanel', views.doctorPanel),
]