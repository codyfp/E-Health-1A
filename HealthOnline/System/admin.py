from django.contrib import admin

from System.models import Prescription, Consultation
# Register your models here.

admin.site.register(Prescription)
admin.site.register(Consultation)

from django.contrib import admin
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

class MapAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
    }