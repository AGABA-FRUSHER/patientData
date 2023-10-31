from Registry.models import RegisteredPatientDetail
from rest_framework import serializers
from .models import Registry

class RegistrySerializer(serializers.ModelSerializer):
    class meta:
        model = Registry
        fields = '__all__'

class RegisteredPatientDetailSerializer(serializers.ModelSerializer):
    class CountrySerializer(serializers.Serializer):
        name = serializers.CharField(max_length=255)

    nationality = CountrySerializer()
    class Meta:
        model = RegisteredPatientDetail
        # fields = '__all__'
        fields = [
            'id',
            'version',
            'birth_date',
            'date_created',
            'first_name',
            'gender',
            'geo_area_level5',
            'id_no',
            'last_name',
            'last_updated',
            'marital_status',
            'nationality',
            'other_name',
            'patient',
            'sub_location',
            'village',
            'ethnicity',
        ]