from django.contrib import admin
from django.urls import path
from . import views, forms
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    # path('register/', views.register_view, name='register'),
    path('register/patient/', views.patient_register_view, name='patient_register'),
    path('register/doctor/', views.doctor_register_view, name='doctor_register'),
    path('<str:user_name>/appointments', views.appointment_view, name='appointments'),
    path('<str:user_name>/schedule', views.schedule_view, name='schedule'),
    path('doctor/<str:user_name>', views.doctor_panel_view, name='doctor_panel'), # You might notice the url   extension looks funny in this one. This is dynamic

    path('appointment/', views.appointment_view, name='appointment'),
    path('schedule/', views.schedule_view, name='schedule'),
    path('doctor/<str:user_name>/prescriptions/', views.create_prescription_view, name='create_prescription'),                                                
    path('<str:user_name>', views.patient_panel_view, name='patient_panel'),
    path('<str:user_name>/prescriptions/', views.list_prescription_view, name='list_prescription'),
    path('doctor/<str:user_name>/profile', views.doctor_profile_view, name='doctor_profile'),
    path('<str:user_name>/profile', views.patient_profile_view, name='patient_profile'),
    
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password_reset.html", form_class=forms.PasswordResetForm), name='reset_password'), 
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
   
    #test page for frontend
    #path('test/', views.test_view, name='test'),
]
