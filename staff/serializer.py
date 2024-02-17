from rest_framework import serializers
from .models import Staff_Model

class staffserializer(serializers.ModelSerializer):
    class Meta:
        model = Staff_Model
        fields = "__all__"