from django.db import models

class Staff_Model(models.Model):
    class Role(models.TextChoices):
        Admin = 'Admin',
        Doctor = 'Doctor',
        Reception= 'Reception',
    

    class status(models.TextChoices):
        Active = 'Active',
        In_active = 'In_active',
    
    name = models.CharField(max_length=25)
    username= models.CharField(max_length = 25)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    role = models.CharField(max_length =9, choices= Role.choices)
    user_status = models.CharField(max_length=9,choices=status.choices)
    password = models.CharField(max_length=15, default="")

    def __str__(self):
        return self.name
# Create your models here.
