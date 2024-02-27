from rest_framework import serializers
from .models import Appointment,Appointment_Detail,payment
from patient.serializer import patientSerializer
# from staff.serializer import staffserializer
from patient.models import Patient_Model
class appointmentserializer(serializers.ModelSerializer):
    patient_id = patientSerializer()
    class Meta:
        model = Appointment
        fields = '__all__'
        # fields = ['date', 'appointment_status', 'note', 'doctor_id', 'patient_id']
    def create(self, validated_data):
        return Appointment.objects.create(**validated_data)
    # def create(self, validated_data):
    #     patient_data = validated_data.pop('patient')
    #     patient_id = patient_data.get('id')
    #     appointment_instance = Appointment.objects.create(patient_id=patient_id, **validated_data)
    #     return appointment_instance
    # class Meta:
    #     model =Appointment
    #     fields = '__all__'
    
    # def create(self, validated_data):
    #     patient_id = validated_data.pop('patient_id')
    #     patient_instance = Patient_Model.objects.get(id=patient_id)
    #     appointment_instance = Appointment.objects.create(patient_id=patient_instance, **validated_data)
    #     return appointment_instance
 
    

class appointment_detailserializer(serializers.ModelSerializer):
    # appointment = appointmentserializer()
    class Meta:
        model =Appointment_Detail
        fields = '__all__'
        
class paymentserializer(serializers.ModelSerializer):
    # appointment = appointmentserializer()
    class Meta:
        model =payment
        fields = '__all__'