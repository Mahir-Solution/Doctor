from django.contrib import admin
from .models import Services_Model

@admin.register(Services_Model)
class servicesadmin(admin.ModelAdmin):
    list_display = ['id','ser_name','price','note']

# Register your models here.
