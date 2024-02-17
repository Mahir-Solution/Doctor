from django.contrib import admin
from .models import Patient_Model
@admin.register(Patient_Model)
class patientadmin(admin.ModelAdmin):
    list_display = ['id','p_name','age','gender','martial_status','phone_no','address','blood_group']
# Register your models here.
