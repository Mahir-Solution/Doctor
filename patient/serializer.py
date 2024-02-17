from rest_framework import serializers
from .models import Patient_Model

class patientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient_Model
        fields = '__all__'