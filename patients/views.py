from rest_framework import viewsets
from .models import Department, Doctor, Patient, Appointment, MedicalRecord, Billing
from .serializers import (
    DepartmentSerializer, DoctorSerializer, PatientSerializer,
    AppointmentSerializer, MedicalRecordSerializer, BillingSerializer
)

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class MedicalRecordViewSet(viewsets.ModelViewSet):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer

class BillingViewSet(viewsets.ModelViewSet):
    queryset = Billing.objects.all()
    serializer_class = BillingSerializer
