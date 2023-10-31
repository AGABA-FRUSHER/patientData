from .import views
# from .views import RegistryViewSet
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'registry', views.RegistryViewSet)
router.register(r'registered-patients', views.RegisteredPatientDetailViewset)



urlpatterns = [
    path('', views.index),
    path('api/', include(router.urls)),
    
]