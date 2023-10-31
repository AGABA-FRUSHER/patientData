from .import views
# from .views import RegistryViewSet
from rest_framework import routers
from django.urls import path, include

router_registry = routers.DefaultRouter()
router_registry.register(r'registry', views.RegistryViewSet)

router_registered_patients = routers.DefaultRouter()
router_registered_patients.register(r'registered-patients', views.RegisteredPatientDetailViewset)



urlpatterns = [
    path('', views.index),
    # path('api/', include(router.urls)),
    path('api/', include(router_registry.urls)),
    path('api/', include(router_registered_patients.urls)),
]