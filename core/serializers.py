from Registry.models import RegisteredPatientDetail
from rest_framework import serializers
from .models import Registry

class RegistrySerializer(serializers.ModelSerializer):
    class meta:
        model = Registry
        fields = '__all__'

class RegisteredPatientDetailSerializer(serializers.ModelSerializer):
    class meta:
        model = RegisteredPatientDetail
        fields = '__all__'