"""HealthOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('System.urls'))
    
    
]

'''
I carried the urls associated with our core app System to System file. 
I was testing one thing but at the end I think this is more organized. 
I think Aryan did this url conf thing like this in the begining but then when 
I changed the file structure it was lost so here it is again. Just go to urls.py
document in System folder to view the rest of the urls and add urls associated with the
System over there from now on.
'''