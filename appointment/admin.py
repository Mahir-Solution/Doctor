from django.contrib import admin
from .models import Appointment,Appointment_Detail,payment


class appointment_detail(admin.TabularInline):
    model = Appointment_Detail
    readonly_fields =('id','Appointment_id','service_id','date','quantity','total')
    extra=0


@admin.register(Appointment)
class appointmentadmin(admin.ModelAdmin):
    list_display = ['id','doctor_id','patient_id','date','appointment_status','note']
    list_filter =['appointment_status']
    inlines =[appointment_detail]


@admin.register(Appointment_Detail)
class appointmentdetail_admin(admin.ModelAdmin):
    list_display =['id','Appointment_id','service_id','date','quantity','total']

@admin.register(payment)
class appointment_payment_admin(admin.ModelAdmin):
    list_display =['id','Appointment_id','date','total','discount','tax','grand_total']
# Register your models here.