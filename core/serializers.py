from Registry.models import Bank, Branch, Company, Country, GeoAreaLevel4, GeoAreaLevel5, LabTest, \
    Patient, RegisteredPatientDetail, PatientLabTest, SystemUser, InvoiceReceipt
from rest_framework import serializers

class SHRPatientRegistrySerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisteredPatientDetail
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    class CompanySerializer(serializers.Serializer):
        id = serializers.IntegerField()
    company = CompanySerializer
    class Meta:
        model = Patient
        fields = ['id', 'company']
        read_only_fields = ['id'] 

class RegisteredPatientDetailSerializer(serializers.ModelSerializer):

    patient = PatientSerializer(required=False)
    class CountrySerializer(serializers.Serializer):
        name = serializers.CharField(max_length=255)

    nationality = CountrySerializer()

    class GeoAreaLevel5Serializer(serializers.Serializer):
        id = serializers.IntegerField(read_only=True)
        name = serializers.CharField(max_length=255)

    geo_area_level5 = GeoAreaLevel5Serializer()
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
class SimpleRegisteredPatientDetailSerializer(serializers.Serializer):
    version = serializers.IntegerField()
    birth_date = serializers.DateTimeField()
    date_created = serializers.DateTimeField()
    first_name = serializers.CharField()
    gender = serializers.CharField()
    geo_area_level5 = serializers.DictField()
    id_no = serializers.CharField()
    last_name = serializers.CharField()
    last_updated = serializers.DateTimeField()
    marital_status = serializers.CharField()
    nationality = serializers.DictField()
    other_name = serializers.CharField()
    patient = serializers.DictField()
    sub_location = serializers.CharField()
    village = serializers.CharField()
    ethnicity = serializers.CharField()
    # def create(self, validated_data):
    #     geo_area_level5_data = validated_data.pop('geo_area_level5', None)
    #     print('g'*100, geo_area_level5_data)
    #     created_by_data = validated_data.pop('created_by', None)
    #     print('c'*100, created_by_data)
    #     geo_area_level4_data = validated_data.pop('geo_area_level4', None)

    #     nationality_data = validated_data.pop('nationality', None)

    #     patient_data = validated_data.pop('patient', {})
    #     print(f'Patient Data: {patient_data}')
    #     branch_data = validated_data.pop('branch', None)
    #     company_data = validated_data.pop('company', None)
    #     print('C'*100, company_data)
    #     created_by_dat = validated_data.pop('created_by', None)
    #     # debtor_account_data = validated_data.pop('debtor_account', None)
    #     employee_account_data = validated_data.pop('employee_account', None)

    #     geo_area_level5_instance, _ = GeoAreaLevel5.objects.update_or_create(**geo_area_level5_data)

    #     if created_by_data:
    #         created_by_instance, _ = SystemUser.objects.update_or_create(**created_by_data)
    #         geo_area_level5_instance.created_by = created_by_instance

    #     if geo_area_level4_data:
    #         geo_area_level4_instance, _ = GeoAreaLevel4.objects.update_or_create(**created_by_data)
    #         geo_area_level5_instance.geo_area_level4 = geo_area_level4_instance


    #     nationality_instance, _ = Country.objects.update_or_create(**nationality_data)

    #     #patient_instance, _ = Patient.objects.update_or_create(registered_patient_detail=registered_patient_detail,**patient_data)
    #     registered_patient_detail = RegisteredPatientDetail.objects.create(
    #         geo_area_level5 = geo_area_level5_instance,
    #         nationality = nationality_instance,
    #         **validated_data
    #     )

    #     if branch_data:
    #         branch_instance, _ = Branch.objects.update_or_create(**branch_data)
    #         patient_instance.branch = branch_instance

    #     if created_by_dat:
    #         created_by_instanc, _ = SystemUser.objects.update_or_create(**created_by_dat)
    #         patient_instance.created_by = created_by_instanc

    #     if employee_account_data:
    #         employee_account_instance, _ = SystemUser.objects.update_or_create(**employee_account_data)
    #         patient_instance.employee_account = employee_account_instance

    #     if company_data:
    #         company_instance = Company.objects.update_or_create(**company_data)
    #         patient_instance.company = company_instance
        
    #     patient_instance, _ = Patient.objects.update_or_create(
    #         registered_patient_detail = registered_patient_detail,
    #         branch = branch_instance,
    #         company = company_instance,
    #         created_by = created_by_instanc,
    #         employee_account = employee_account_instance,
    #         **patient_data
    #     )
    #     print('P'*100, patient_instance)
            
    #     registered_patient_detail.save()

    #     return registered_patient_detail
            


    # def create(self, validated_data):
    #     print('!' * 100, validated_data)
    #     patient_data = validated_data.pop('patient', None)
    #     nationality_data = validated_data.pop('nationality', None)
    #     geo_area_level5_data = validated_data.pop('geo_area_level5', None)
    #     print('p' * 100, patient_data)

    #     nationality_instance, _ = Country.objects.update_or_create(**nationality_data)
    #     print('n' * 100, nationality_instance)
    #     try:
    #         geo_area_level5_instance = GeoAreaLevel5.objects.get(**geo_area_level5_data)
    #     except GeoAreaLevel5.DoesNotExist:
    #         print('GeoAreaLevel5.DoesNotExist exception triggered.')
    #         print('GeoAreaLevel5 data:', geo_area_level5_data)
    #         geo_area_level5_instance = GeoAreaLevel5.objects.create(**geo_area_level5_data)
    #         print('Created GeoAreaLevel5 instance:', geo_area_level5_instance)
    #         print('g' * 100, geo_area_level5_instance)

    #     # geo_area_level5_instance, _ = GeoAreaLevel5.objects.update_or_create(**geo_area_level5_data)
    #     registered_patient_detail = RegisteredPatientDetail.objects.create(
    #         nationality=nationality_instance,
    #         geo_area_level5=geo_area_level5_instance,
    #         version=validated_data.get('version', 0),  # Set a default value if not provided
    #         **validated_data
    #     )

    #     print('-' * 100, registered_patient_detail)

    #     if patient_data:
    #         patient_instance = Patient.objects.create(**patient_data)

    #         registered_patient_detail.patient = patient_instance
    #         registered_patient_detail.save()

    #         patient_serializer = PatientSerializer(patient_instance)
    #         registered_patient_detail.patient = patient_serializer.data

    #     return registered_patient_detail

    

    # def create(self, validated_data):
    #     nationality_data = validated_data.pop('nationality', None)
    #     geo_area_level5 = validated_data.pop('geo_area_level5', None)

    #     nationality_instance, _ = Country.objects.update_or_create(**nationality_data)
    #     geo_area_level5_instance, _ = GeoAreaLevel5.objects.update_or_create(**geo_area_level5)

    #     patient_data = validated_data.pop('patient', None)
    #     patient_instance = Patient.objects.create(**patient_data)

    #     registered_patient_detail = RegisteredPatientDetail.objects.create(
    #         patient=patient_instance,
    #         nationality=nationality_instance,
    #         geo_area_level5=geo_area_level5_instance,
    #         **validated_data
    #     )

    #     return registered_patient_detail
class InvoiceReceiptSerializer(serializers.ModelSerializer):

    class BankSerializer(serializers.Serializer):
        class Meta:
            model = Bank
            fields = ['name']
        # name = serializers.CharField(max_length=255)
    # bank = BankSerializer()
    class Meta:
        model = InvoiceReceipt
        
        fields = [
            'id',
            'version',
            'prn',
            'bank_branch',
            'bank_transaction_id',
            'bank',
            'currency_code',
            'paymentStatus',
            'bank_code',
            'amount',
            'branch',
            'company',
            'created_by',
            'credited_account',
            'date_created',
            'debited_account',
            'description',
            'employee_debt',
            'invoice_line',
            'last_updated',
            'patient',
            'payment_date',
            'receipt_type',
            'transaction_fee_account',
            'transaction_id',
            'void_status'
        ]



class SimpleInvoiceReceiptSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    version = serializers.IntegerField()
    prn = serializers.CharField(allow_null=True, required=False)
    bank_branch = serializers.CharField()
    bank_transaction_id = serializers.IntegerField()
    bank = serializers.DictField()
    currency_code = serializers.CharField()
    paymentStatus = serializers.CharField()
    bank_code = serializers.CharField()
    amount = serializers.IntegerField()
    branch = serializers.DictField()
    company = serializers.DictField()
    created_by = serializers.DictField()
    credited_account = serializers.DictField()
    date_created = serializers.DateField()
    debited_account = serializers.DictField()
    description = serializers.CharField()
    employee_debt = serializers.DictField()
    invoice_line = serializers.DictField()
    last_updated = serializers.DateField()
    patient = serializers.DictField()
    payment_date = serializers.DateField()
    receipt_type = serializers.CharField()
    transaction_fee_account = serializers.DictField()
    transaction_id = serializers.DictField()
    void_status = serializers.CharField()

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
            'lab_test',
            'status'
        ]


