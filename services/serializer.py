from rest_framework import serializers
from .models import Services_Model
class servicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services_Model
        fields = ['id','ser_name','price','note']