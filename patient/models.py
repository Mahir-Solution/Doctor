from django.db import models

class Patient_Model(models.Model):
    class BloodGroup(models.TextChoices):
        A_POSITIVE = 'A+', 
        A_NEGATIVE = 'A-', 
        B_POSITIVE = 'B+', 
        B_NEGATIVE = 'B-', 
        O_POSITIVE = 'O+', 
        O_NEGATIVE = 'O-', 
        AB_POSITIVE = 'AB+', 
        AB_NEGATIVE = 'AB-', 
        UN_KNOWN = 'UN_KNOWN',
    class Gender(models.TextChoices):
        Male = 'Male',
        Female = 'Female',
        Other = 'Other',
    class Martial(models.TextChoices):
        UnMarried = 'UnMarried',
        Married = 'Married',
    
    p_name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=6, choices=Gender.choices )
    martial_status = models.CharField(max_length =9,choices = Martial.choices)
    phone_no = models.CharField(max_length =20)
    address = models.CharField(max_length = 150)
    blood_group = models.CharField(max_length=8, choices=BloodGroup.choices)
    
    def __str__(self):
        return self.p_name
# Create your models here.
