from .import views
# from .views import RegistryViewSet
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'registry', views.RegistryViewSet)
router.register(r'registered-patients-details', views.RegisteredPatientDetailViewset)
router.register(r'lab-tests', views.LabTestViewset)
router.register(r'patient-lab-tests', views.PatientLabTestViewset)
router.register(r'lab-tests-datails', views.RegisteredPatientDetailSimpleViewset)
router.register(r'lab-tests-result-datails', views.PatientLabTestResultViewSet)




urlpatterns = [
    path('eafya/', include(router.urls)),
    # path('eafya/patient-lab-tests/<int:pk>/update/', 
            # views.PatientLabTestViewset.as_view({'put': 'update'}), name='patient-lab-test-update'),
    path('eafya/lab-tests-result-details/<int:pk>/update/', 
            views.PatientLabTestResultViewSet.as_view({'put': 'update'}), name='lab-test-result-update'),
]