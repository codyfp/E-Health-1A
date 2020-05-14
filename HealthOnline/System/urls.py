from django.contrib import admin
from django.urls import path
from . import views, forms
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('register/patient/', views.patient_register_view, name='patient_register'),
    path('register/doctor/', views.doctor_register_view, name='doctor_register'),
    
    path('doctor-<str:user_name>', views.doctor_panel_view, name='doctor_panel'), 
    path('doctor-<str:user_name>/prescriptions/', views.doctor_prescription_view, name='doctor_prescription'), 
                                                                                  
    path('<str:user_name>', views.patient_panel_view, name='patient_panel'),
    path('<str:user_name>/prescriptions/', views.patient_prescription_view, name='patient_prescription'), 
    
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password_reset.html", form_class=forms.PasswordResetForm), name='reset_password'), 

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
   
    #test page for frontend
    path('test/', views.test_view, name='test'),
]
