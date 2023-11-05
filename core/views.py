from django.shortcuts import render
from Registry.models import LabTest, RegisteredPatientDetail, PatientLabTest
from core.filters import PatientLabTestFilter
from rest_framework import viewsets, status
from .models import Registry
from .serializers import LabTestSerializer, RegisteredPatientDetailSerializer, RegisteredPatientDetailSimpleSerializer, RegistrySerializer, PatientLabTestSerializer
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.utils import timezone
from rest_framework.exceptions import ValidationError


class RegistryViewSet(viewsets.ModelViewSet):
    queryset = Registry.objects.all()
    serializer_class = RegistrySerializer


class RegisteredPatientDetailViewset(viewsets.ModelViewSet):
    queryset = RegisteredPatientDetail.objects.all()
    serializer_class = RegisteredPatientDetailSerializer


class LabTestViewset(viewsets.ModelViewSet):
    queryset = LabTest.objects.all()
    serializer_class = LabTestSerializer

    # def create(self, request, *args, **kwargs):
    #     lab_test_instance = request.data
    #     serializer = self.get_serializer(data=lab_test_instance)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PatientLabTestViewset(viewsets.ModelViewSet):
    queryset = PatientLabTest.objects.all().order_by('-date_created')
    pagination_class = PageNumberPagination
    serializer_class = PatientLabTestSerializer
    filter_class = PatientLabTestFilter
    page_size = 10
    # def get_queryset(self):
        # queryset = PatientLabTest.objects.all().order_by('-date_created')

        # since_param = self.request.query_params.get('since')
        # if since_param:
        #     try:
        #         since_datetime = timezone.datetime.fromisoformat(since_param)
        #         queryset = queryset.filter(date_created__gte=since_datetime)
        #     except ValueError:
        #         pass

        # return queryset
    
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

