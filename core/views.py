from django.shortcuts import render
from Registry.models import RegisteredPatientDetail
from rest_framework import viewsets
from .models import Registry
from .serializers import RegisteredPatientDetailSerializer, RegistrySerializer

# Create your views here.

def index(request):
    query_set = Registry.objects.all()
    print('*'*100, query_set)
    context = {'query_set': query_set}
    return render(request, 'index.html', context)


class RegistryViewSet(viewsets.ModelViewSet):
    queryset = Registry.objects.all()
    print('='*100, queryset)
    serializer_class = RegistrySerializer

class RegisteredPatientDetailViewset(viewsets.ModelViewSet):
    queryset = RegisteredPatientDetail.objects.all()
    serializer_class = RegisteredPatientDetailSerializer

