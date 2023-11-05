import django_filters
from Registry.models import PatientLabTest

# filters.py

class PatientLabTestFilter(django_filters.FilterSet):
    since = django_filters.IsoDateTimeFilter(field_name="date_created", lookup_expr="gte")

    class Meta:
        model = PatientLabTest
        fields = []
