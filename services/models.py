from django.db import models

class Services_Model(models.Model):
    ser_name = models.CharField(max_length=150)
    price = models.DecimalField(default = 0.0, max_digits=8, decimal_places=2)
    note = models.TextField()

    def __str__(self):
        return self.ser_name


# Create your models here.
