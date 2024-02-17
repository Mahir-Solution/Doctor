from django.db import models
from patient.models import Patient_Model
from staff.models import Staff_Model
from django.utils import timezone
from services.models import Services_Model
class Appointment(models.Model):
    class patient_status(models.TextChoices):
        waiting = 'waiting',
        progress_in ='progress_in',
        complete = 'complete',
        cancel = 'cancel',
    
    doctor_id =models.ForeignKey(Staff_Model, verbose_name=("Doctor"), on_delete=models.CASCADE, null=True)
    patient_id= models.ForeignKey(Patient_Model, verbose_name=("Patient"), on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=False,default=timezone.now)
    appointment_status = models.CharField(max_length=11, choices =patient_status.choices)
    note = models.TextField(null=True)
    
    def __str__(self):
        return str(self.id)


class Appointment_Detail(models.Model):
    Appointment_id= models.ForeignKey(Appointment, verbose_name=("Appointment"), on_delete=models.CASCADE)
    service_id = models.ForeignKey(Services_Model, verbose_name=("Service"), on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=False,default=timezone.now)
    quantity = models.IntegerField()
    total = models.IntegerField()
    
    def sub_total(self):
        return self.service_id.price*self.quantity
    def __str__(self):
        return str(self.Appointment_id.id)
        
class payment(models.Model):
    class payment_status(models.TextChoices):
        complete='complete',
        partial ='partial',
    Appointment_id= models.ForeignKey(Appointment, verbose_name=("Appointment"), on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    total= models.IntegerField()
    discount=models.IntegerField(default=0)
    tax=models.IntegerField(default=0)
    grand_total=models.IntegerField()
# Create your models here.
