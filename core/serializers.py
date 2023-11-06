from Registry.models import LabTest, RegisteredPatientDetail, PatientLabTest, SystemUser
from rest_framework import serializers
from .models import Registry

class RegistrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Registry
        fields = '__all__'

class RegisteredPatientDetailSerializer(serializers.ModelSerializer):
    class CountrySerializer(serializers.Serializer):
        name = serializers.CharField(max_length=255)

    nationality = CountrySerializer()
    class Meta:
        model = RegisteredPatientDetail
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

class LabTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabTest
        fields = '__all__'


class PatientLabTestSerializer(serializers.ModelSerializer):
    patient_details = serializers.SerializerMethodField()
    class LabTestSerializer(serializers.ModelSerializer):
        class Meta:
            model = LabTest
            fields = [
                'name',
                'id',
            ]
    lab_test = LabTestSerializer()
    class SytemUserSerializer(serializers.ModelSerializer):
        class Meta:
            model = SystemUser
            fields = [
                'first_name',
            ]
    created_by = SytemUserSerializer()
    class Meta:
        model = PatientLabTest
        fields = '__all__'
        # fields = [
        #     'parent_id',
        #     'lab_test',
        #     'patient_details',
        #     'created_by',
        #     'date_created',
        #     'result',
        #     'id',
        # ]
    def get_patient_details(self, obj):
        registered_patient_detail = obj.encounter.clinic_session.patient_visit.patient.registeredpatientdetail
        return {
            'first_name': registered_patient_detail.first_name,
            'patient_id': registered_patient_detail.patient_id,
            'birth_date': registered_patient_detail.birth_date,
            'id': registered_patient_detail.id,
            'date_created': registered_patient_detail.date_created,
            'id_no': registered_patient_detail.id_no,
            'last_name': registered_patient_detail.last_name,
            'last_updated': registered_patient_detail.last_updated,
            'marital_status': registered_patient_detail.marital_status,
            'nationality': registered_patient_detail.nationality.name,
            'other_name': registered_patient_detail.other_name,
            'sub_location': registered_patient_detail.sub_location,
            'village': registered_patient_detail.village,
            'ethnicity': registered_patient_detail.ethnicity,
            'gender': registered_patient_detail.gender,
        }


class PatientLabSerializer(serializers.ModelSerializer):
    class LabTestSerializer(serializers.ModelSerializer):
        class Meta:
            model = LabTest
            fields = [
                'name',
                'description',
                'id'
            ]
    lab_test = LabTestSerializer()

    class SytemUserSerializer(serializers.ModelSerializer):
        class Meta:
            model = SystemUser
            fields = [
                'first_name',
            ]
    created_by = SytemUserSerializer()


    class Meta:
        model = PatientLabTest
        fields = [
            'lab_test',
            'date_created',
            'created_by',
        ]
class RegisteredPatientDetailSimpleSerializer(serializers.ModelSerializer):

    # patient_lab_tests = PatientLabSerializer(many=True, source='get_patient_lab_tests')
    # patient = PatientLabSerializer(source='patient.patientvisit_set')
    patient_lab_tests = serializers.SerializerMethodField()

    class Meta:
        model = RegisteredPatientDetail
        fields = [
            'id',
            'first_name',
            'last_name',
            'patient',
            'birth_date',
            'date_created',
            'gender',
            'last_updated',
            'ethnicity',
            'patient_lab_tests',
        ]

    def get_patient_lab_tests(self, obj):
        
        # lab_tests = obj.patient.patientvisit_set.last().clinicsession_set.last().encounter_set.last().patientlabtest_set.all()
        lab_tests = PatientLabTest.objects.filter(encounter__clinic_session__patient_visit__patient_id=obj.patient_id)

        return PatientLabSerializer(lab_tests, many=True, context=self.context).data
    

class PatientLabTestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientLabTest
        fields = [
            'id',
            'result',
            'parent_id',
            'lab_test'
        ]


