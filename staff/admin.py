from django.contrib import admin
from .models import Staff_Model
@admin.register(Staff_Model)
class staffaddmin(admin.ModelAdmin):
    list_display = ['id','name','username','email','phone','role','user_status']
# Register your models here.
