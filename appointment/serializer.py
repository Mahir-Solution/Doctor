from rest_framework import serializers
from .models import Appointment,Appointment_Detail,payment
class appointmentserializer(serializers.ModelSerializer):
    class Meta:
        model =Appointment
        fields = '__all__'

class appointment_detailserializer(serializers.ModelSerializer):
    class Meta:
        model =Appointment_Detail
        fields = '__all__'

class paymentserializer(serializers.ModelSerializer):
    class Meta:
        model =payment
        fields = '__all__'