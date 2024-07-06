from django.shortcuts import render
from Registry.models import Bank, Company, EmployeeDebt, GeneralJournal, InvoiceLine, LabTest, Patient, RegisteredPatientDetail, PatientLabTest, \
    Branch, SystemUser, GeoAreaLevel5, Country, InvoiceReceipt
from core.filters import PatientLabTestFilter
from rest_framework import viewsets, status
from .serializers import LabTestSerializer, PatientLabTestResultSerializer, PatientSerializer, \
    RegisteredPatientDetailSerializer, RegisteredPatientDetailSimpleSerializer, SHRPatientRegistrySerializer, \
        PatientLabTestSerializer, SimpleRegisteredPatientDetailSerializer, InvoiceReceiptSerializer, \
        SimpleInvoiceReceiptSerializer
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.utils import timezone
from rest_framework.exceptions import ValidationError
from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView




import base64
import json
import os
import requests
from dotenv import load_dotenv
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes as crypto_hashes
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography import x509
from dotenv import load_dotenv
import xml.etree.ElementTree as ET


# Load env variables
load_dotenv('/home/frusher/Desktop/patientRegistry/patientData/core/test.env')

# Constants
username = os.getenv('EAFYA')
password = os.getenv('EAFYAPWD')
ura_certificate_path = os.getenv('URA_CERTIFICATE_PATH', '/home/frusher/Desktop/patientRegistry/patientData/Registry/ura.cer')
private_key_path = os.getenv('PRIVATE_KEY_PATH', '/home/frusher/Desktop/patientRegistry/patientData/core/eafya.privkey.pem')
private_key_password = os.getenv('PRIVATE_KEY_PASSWORD', 'EAFYAPWD')

concatenated_credentials = f'{username}{password}'


def encryption(concatenated_creds, public_key_path='/home/frusher/Desktop/patientRegistry/patientData/core/eafya.pubkey.pem'):
    '''
    Function to encrypt concatenated (username + password) with URA public Key
    '''
    with open(public_key_path, 'rb') as cert_file:
        cert_data = cert_file.read()
        cert = x509.load_pem_x509_certificate(cert_data, default_backend())
        public_key = cert.public_key()
    
    encrypted = public_key.encrypt(
        concatenated_creds.encode('utf-8'),
        padding.PKCS1v15()
    )

    return base64.b64encode(encrypted)

def signature(encrypted, key_path, key_password):
    '''
    Function to sign encrypted data with MDA private key and private key password
    '''
    with open(key_path, 'rb') as private_key_file:
        try:
            # Attempt to load the private key with the provided password
            private_key = serialization.load_pem_private_key(
                private_key_file.read(),
                password=key_password.encode('utf-8'),
                backend=default_backend()
            )
        except ValueError:
            print("Error: Incorrect password or private key is not encrypted.")
            return None
    
    signed = private_key.sign(
        encrypted,
        padding.PKCS1v15(),
        crypto_hashes.SHA1()
    )

    signed_credentials = base64.b64encode(signed).decode('utf-8')

    return signed_credentials


def get_access_token():
    token_url = "https://helpdesk.health.go.ug/token"
    
    token_headers = {
        "Authorization": "Basic VmFOTVNYSjBZQ1VZOWg1cVJ0SFFoRG5JaVJvYTptUG41WUZ4VHBabFZEeFZIYzBkQXVTU2RxWVVh",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    token_data = {
        "grant_type": "client_credentials"
    }
    
    response = requests.post(token_url, headers=token_headers, data=token_data)
    
    if response.status_code == 200:
        token_response = response.json()
        return token_response['access_token']
    else:
        raise Exception(f"Failed to get access token: {response.status_code} {response.text}")
    

def check_prn(PRN, encrypted_credentials, signed_credentials):
    endpoint_url = "https://helpdesk.health.go.ug/checkprn"

    payload = {
        "CheckPRNStatus": {
        "strPRN": PRN,
        "concatenatedUsernamePasswordSignature": signed_credentials,
        "encryptedConcatenatedUsernamePassword": encrypted_credentials,
        "userName": "EAFYA"
        }
    }

    access_token = get_access_token()

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        # "scope": "default",
        # "token_type": "Bearer",
        "Authorization": f"Bearer {access_token}",
        "Allow": "POST, OPTIONS"

    }

    payload_jsn_str = json.dumps(payload)    
    response = requests.post(endpoint_url, data=payload_jsn_str, headers=headers)
    if response.status_code == 200:
        try:
            return response.json()
        except json.decoder.JSONDecodeError:
            return {"error": "Response is not in JSON format"}
    else:
        return {"error": "Failed to check PRN", "status_code": response.status_code, "details": response.text}

def get_prn(data, encrypted_credentials, signed_credentials):
    '''
    Function to send the request with encrypted and signed credentials
    '''
    endpoint_url = "https://helpdesk.health.go.ug/getprn"

    payload = {
                "PRNRequest":{
                "AdditionalFees":"0",
                "Amount":data["amount"],
                "AssessmentDate":data["date_created"],
                "BuildingName":None,
                "ContactNo":None,
                "County":None,
                "District":None,
                # "Email":data["email"],
                "ExpiryDays":"21",
                "ForeignCurrencyCode":None,
                "GrossAmount":"0",
                "LocalCouncil":None,
                # "MobileNo":"256779825056",
                "NoOfForms":"0",
                "Parish":None,
                "PaymentBankCode":"DTB",
                "PaymentMode":"CASH",
                "PaymentType":"DT",
                "PlotNo":None,
                "ReferenceNo":data["transaction_id"]["id"],
                "SRCSystem":"EAFYA SYSTEM",
                "Street":None,
                "SubCounty":None,
                "TIN":"1000035867",
                "TaxHead":"KCCA524",
                "TaxPayerBankCode":"DTB",
                "TaxPayerName":data["company"]["name"],
                "TaxSubHead":None,
                "TraceCentre":None,
                "Village":None, 
                },
                "concatenatedUsernamePasswordSignature": signed_credentials,
                "encryptedConcatenatedUsernamePassword": encrypted_credentials,
                "userName": "EAFYA"
            }

    access_token = get_access_token()
    print('|'*100, payload)

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "scope": "default",
        "token_type": "Bearer",
        "Authorization": f"Bearer {access_token}"

    }

    payload_jsn_str = json.dumps(payload)    
    response = requests.post(endpoint_url, data=payload_jsn_str, headers=headers)

    json_response = response.json()
    prn_value = json_response['GetPRNResponse']['GetPRNResult']['PRN']
    return prn_value


def get_company_instance_by_id(company_id):
    # Replace this with your actual logic to retrieve a Company instance
    return get_object_or_404(Company, id=company_id)

class RegistryViewSet(viewsets.ModelViewSet):
    queryset = RegisteredPatientDetail.objects.all()
    print('|'*100, queryset)
    serializer_class = SHRPatientRegistrySerializer


class CheckPRNAPIView(APIView):

    def post(self, request, *args, **kwargs):
        data = request.data
        prn = data.get("PRN")
        print('?'*100, prn)

        if not prn:
            return Response({"error": "PRN is required"}, status=status.HTTP_400_BAD_REQUEST)

        encrypted_data = encryption(concatenated_credentials, ura_certificate_path)
        encrypted_credentials = encrypted_data.decode('utf-8')
        signed_credentials = signature(encrypted_data, private_key_path, private_key_password)

        # Check PRN
        check_prn_response = check_prn(prn, encrypted_credentials, signed_credentials)
        print('!'*100,check_prn_response)

        if not check_prn_response or "error" in check_prn_response:
            return Response(check_prn_response, status=status.HTTP_400_BAD_REQUEST)

        return Response(check_prn_response, status=status.HTTP_200_OK)


class InvoiceReceiptCreateAPIView(CreateAPIView):
    queryset = InvoiceReceipt.objects.all()
    serializer_class = InvoiceReceiptSerializer

    def get_or_none(self, model, **kwargs):
        try:
            return model.objects.get(**kwargs)
        except model.DoesNotExist:
            return None

    def create(self, request, *args, **kwargs):
        data = request.data
        print('$'*100, data)
        serializer = SimpleInvoiceReceiptSerializer(data=data)
        if not serializer.is_valid():
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
        encrypted_data = encryption(concatenated_credentials, ura_certificate_path)
        encrypted_credentials = encrypted_data.decode('utf-8')
        signed_credentials = signature(encrypted_data, private_key_path, private_key_password)
        generated_prn_get_prn = get_prn(data, encrypted_credentials, signed_credentials)

        id = data.get('id')
        version = data.get('version')
        prn = generated_prn_get_prn
        bank_branch = data.get('bank_branch')
        bank_transaction_id = data.get('bank_transaction_id')
        bank = data.get('bank')
        currency_code = data.get('currency_code')
        paymentStatus = data.get('paymentStatus')
        bank_code = data.get('bank_code')
        amount = data.get('amount')
        branch = data.get('branch')
        company = data.get('company')
        created_by = data.get('created_by')
        credited_account = data.get('credited_account')
        date_created = data.get('date_created')
        debited_account = data.get('debited_account')
        description = data.get('description')
        employee_debt = data.get('employee_debt')
        invoice_line = data.get('invoice_line')
        last_updated = data.get('last_updated')
        patient = data.get('patient')
        payment_date = data.get('payment_date')
        receipt_type = data.get('receipt_type')
        transaction_fee_account = data.get('transaction_fee_account')
        transaction_id = data.get('transaction_id')
        void_status = data.get('void_status')
        employee_debt_instance = None if not employee_debt else self.get_or_none(EmployeeDebt, id=employee_debt['id'])


        obj = InvoiceReceipt.objects.create(
            id = id,
            version = version,
            prn = prn,
            bank_branch = bank_branch,
            bank_transaction_id = bank_transaction_id,
            bank = Bank.objects.get(name=bank['name']),
            currency_code = currency_code,
            paymentStatus = paymentStatus,
            bank_code = bank_code,
            amount = amount,
            branch = Branch.objects.get(id=branch['id']),
            company = Company.objects.get(name=company['name']),
            created_by = SystemUser.objects.get(first_name=created_by['first_name']),
            credited_account = GeneralJournal.objects.get(id=credited_account['id']),
            date_created = date_created,
            debited_account = GeneralJournal.objects.get(id=credited_account['id']),
            description = description,
            # employee_debt = EmployeeDebt.objects.get(id=employee_debt['id']),
            employee_debt=employee_debt_instance,
            invoice_line = InvoiceLine.objects.get(id=invoice_line['id']),
            last_updated = last_updated,
            patient = Patient.objects.get(id=patient['id']),
            payment_date = payment_date,
            receipt_type = receipt_type,
            transaction_fee_account = GeneralJournal.objects.get(id=transaction_fee_account['id']),
            transaction_id = GeneralJournal.objects.get(id=transaction_id['id']),
            void_status = void_status,
        )

        response_serializer = InvoiceReceiptSerializer(obj).data
        print('prn_value:', response_serializer)
        return Response(response_serializer, status=status.HTTP_201_CREATED)



    # def create(self, request, *args, **kwargs):
    #     data = request.data
    #     print('$'*100, data)
    #     serializer = SimpleInvoiceReceiptSerializer(data=data)
    #     if not serializer.is_valid():
    #         return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    #     encrypted_data = encryption(concatenated_credentials, ura_certificate_path)
    #     encrypted_credentials = encrypted_data.decode('utf-8')
    #     signed_credentials = signature(encrypted_data, private_key_path, private_key_password)
    #     generated_prn_get_prn = get_prn(data, encrypted_credentials, signed_credentials)

    #     # Fetch the existing instance
    #     id = data.get('id')
    #     try:
    #         invoice_receipt = InvoiceReceipt.objects.get(id=id)
    #         invoice_receipt.prn = generated_prn_get_prn
    #         invoice_receipt.save()

    #         response_serializer = InvoiceReceiptSerializer(invoice_receipt).data
    #         print('prn_value:', response_serializer)
    #         return Response(response_serializer, status=status.HTTP_200_OK)

    #     except InvoiceReceipt.DoesNotExist:
    #         return Response({'error': 'InvoiceReceipt with the given ID does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        

class RegisteredPatientDetailCreateAPIView(CreateAPIView):
    queryset = RegisteredPatientDetail.objects.all()
    serializer_class = RegisteredPatientDetailSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = SimpleRegisteredPatientDetailSerializer(data=data)
        if not serializer.is_valid():
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        version = data.get('version')
        birth_date = data.get('birth_date')
        date_created = data.get('date_created')
        first_name = data.get('first_name')
        gender = data.get('gender')
        geo_area_level5 = data.get('geo_area_level5')
        id_no = data.get('id_no')
        last_name = data.get('last_name')
        last_updated = data.get('last_updated')
        marital_status = data.get('marital_status')
        nationality = data.get('nationality')
        other_name = data.get('other_name')
        # patient = data.get('patient')
        sub_location = data.get('sub_location')
        village = data.get('village')
        ethnicity = data.get('ethnicity')

        patient_obj = Patient.objects.create(
            version=version,
            # address=address,
            branch=Branch.objects.get(id=1),
            # city=city,
            company=Company.objects.get(id=1),
            # company=company['name'],
            # created_by=created_by['first_name'],
            created_by=SystemUser.objects.get(id=1),
            date_created=date_created,
            # debtor_account=debtor_account,
            # email=email,
            # employee_account=employee_account['first_name'],
            last_updated=last_updated,
            partner_type='partner_type',
            phone_number=0,
            # postal_code=postal_code,
        )
        print('>'*100,patient_obj)
        obj = RegisteredPatientDetail.objects.create(
            version=version,
            birth_date=birth_date,
            date_created=date_created,
            first_name=first_name,
            gender=gender,
            geo_area_level5=GeoAreaLevel5.objects.get(name=geo_area_level5['name']),
            id_no=id_no,
            last_name=last_name,
            last_updated=last_updated,
            marital_status=marital_status,
            other_name=other_name,
            patient=patient_obj,
            sub_location=sub_location,
            village=village,
            ethnicity=ethnicity,
            nationality=Country.objects.get(name=nationality['name']),
        )
        print('Data before object creation:', data)
        print('='*100, obj.patient)
        response_serilizer = RegisteredPatientDetailSerializer(obj).data
        return Response(response_serilizer, status=status.HTTP_201_CREATED)


class LabTestViewset(viewsets.ModelViewSet):
    queryset = LabTest.objects.all().order_by('id')
    serializer_class = LabTestSerializer

    def create(self, request, *args, **kwargs):
        lab_test_instance = request.data
        serializer = self.get_serializer(data=lab_test_instance)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PatientLabTestViewset(viewsets.ModelViewSet):
    queryset = PatientLabTest.objects.all().order_by('-date_created')
    pagination_class = PageNumberPagination
    serializer_class = PatientLabTestSerializer
    filter_class = PatientLabTestFilter
    page_size = 10
    def get_queryset(self):
        queryset = PatientLabTest.objects.filter(parent_id=0).order_by('-date_created')

        since_param = self.request.query_params.get('since')
        if since_param:
            try:
                since_datetime = timezone.datetime.fromisoformat(since_param)
                queryset = queryset.filter(date_created__gte=since_datetime)
            except ValueError:
                pass

        return queryset
    
    def update(self, request, pk=None):
        try:
            patient_lab_test = PatientLabTest.objects.get(pk=pk)
            
            parent_id = request.data.get('parent_id')
            if parent_id != patient_lab_test.parent_id:
                raise ValidationError("Parent ID does not match.")
            
            lab_test_id = request.data.get('lab_test')['id']
            if lab_test_id != patient_lab_test.lab_test.id:
                raise ValidationError("Lab Test ID does not match.")
            
            if patient_lab_test.result is not None:
                raise ValidationError("Result is not null.")
            
            patient_lab_test.result = request.data.get('result')
            patient_lab_test.save()
            
            serializer = PatientLabTestSerializer(patient_lab_test)
            return Response(serializer.data)
        
        except PatientLabTest.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class RegisteredPatientDetailSimpleViewset(viewsets.ModelViewSet):
    queryset = RegisteredPatientDetail.objects.all().order_by('-date_created')
    serializer_class = RegisteredPatientDetailSimpleSerializer
    pagination_class = PageNumberPagination


class PatientLabTestResultViewSet(viewsets.ModelViewSet):
    queryset = PatientLabTest.objects.all()
    serializer_class = PatientLabTestResultSerializer

    def update(self, request, pk=None):
        try:
            patient_lab_test_id = pk
            results = request.data
            for result in results:
                patient_lab_test = PatientLabTest.objects.filter(
                    (Q(id=patient_lab_test_id) | Q(parent_id=patient_lab_test_id)) &
                    Q(lab_test=result['lab_test_id'])
                )
                print('*'*100, patient_lab_test.query)

                # patient_lab_test.update(result=result['result'])
                patient_lab_test.update(result=result['result'], status='Tested')
                print(result, results, '#'*100)

            return Response({'message': 'Lab test result updated successfully.'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

