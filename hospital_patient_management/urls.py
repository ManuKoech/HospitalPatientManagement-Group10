from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from patients.views import (
    DepartmentViewSet, DoctorViewSet, PatientViewSet,
    AppointmentViewSet, MedicalRecordViewSet, BillingViewSet
)


router = routers.DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'doctors', DoctorViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'medical-records', MedicalRecordViewSet)
router.register(r'billings', BillingViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    
]
