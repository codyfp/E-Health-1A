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
<<<<<<< HEAD
    path('<str:user_name>/appointments', views.appointment_view, name='appointments'),
    path('<str:user_name>/schedule', views.schedule_view, name='schedule'),
    path('doctor/<str:user_name>', views.doctor_panel_view, name='doctor_panel'), # You might notice the url   extension looks funny in this one. This is dynamic
                                                                                  # url conf. in django. Google it if you haven't heard it before.
                                                                                  # Note: user_name is a parameter here and it is passed to associated view function.
                                                                                  # The place I actually do the parameter passing tho is login function in redirect() function.
                                                                                  # I.e. check for user_name variable in the places I mentioned. 
=======
    
    path('doctor-<str:user_name>', views.doctor_panel_view, name='doctor_panel'), 
    path('doctor-<str:user_name>/prescriptions/', views.doctor_prescription_view, name='doctor_prescription'), 
>>>>>>> 8503a5717d65260ef02e3e0f98876becd863eaed
                                                                                  
    path('<str:user_name>', views.patient_panel_view, name='patient_panel'),
    path('<str:user_name>/prescriptions/', views.patient_prescription_view, name='patient_prescription'), 
    
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password_reset.html", form_class=forms.PasswordResetForm), name='reset_password'), 

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
   
    #test page for frontend
    path('test/', views.test_view, name='test'),
]
