from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.utils import timezone
from .models import Department, Doctor, Patient, Appointment, MedicalRecord, Billing

class APITestSetup(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Departments
        self.department = Department.objects.create(
            name="Cardiology",
            description="Heart department"
        )

        # Doctors
        self.doctor = Doctor.objects.create(
            first_name="Alice",
            last_name="Smith",
            specialization="Cardiologist",
            phone_number="0712345678",
            email="alice@example.com",
            department=self.department
        )

        # Patients
        self.patient = Patient.objects.create(
            first_name="John",
            last_name="Doe",
            date_of_birth="1990-01-01",
            phone_number="0798765432",
            email="john@example.com",
            address="123 Nairobi St"
        )

        # Appointments
        self.appointment = Appointment.objects.create(
            patient=self.patient,
            doctor=self.doctor,
            date=timezone.now(),
            reason="Regular checkup",
            status="Scheduled"
        )

        # Medical Records
        self.medical_record = MedicalRecord.objects.create(
            patient=self.patient,
            doctor=self.doctor,
            diagnosis="Healthy",
            treatment="None"
        )

        # Billing
        self.billing = Billing.objects.create(
            patient=self.patient,
            appointment=self.appointment,
            amount=5000,
            payment_status="Pending"
        )


class DepartmentTests(APITestSetup):
    def test_get_departments(self):
        response = self.client.get(reverse('department-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_department(self):
        data = {"name": "Neurology", "description": "Brain department"}
        response = self.client.post(reverse('department-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class DoctorTests(APITestSetup):
    def test_get_doctors(self):
        response = self.client.get(reverse('doctor-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_doctor(self):
        data = {
            "first_name": "Bob",
            "last_name": "Brown",
            "specialization": "Neurologist",
            "phone_number": "0700112233",
            "email": "bob@example.com",
            "department": self.department.id
        }
        response = self.client.post(reverse('doctor-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class PatientTests(APITestSetup):
    def test_get_patients(self):
        response = self.client.get(reverse('patient-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_patient(self):
        data = {
            "first_name": "Mary",
            "last_name": "Jane",
            "date_of_birth": "1995-05-05",
            "phone_number": "0711122233",
            "email": "mary@example.com",
            "address": "456 Nairobi St"
        }
        response = self.client.post(reverse('patient-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class AppointmentTests(APITestSetup):
    def test_get_appointments(self):
        response = self.client.get(reverse('appointment-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_appointment(self):
        data = {
            "patient": self.patient.id,
            "doctor": self.doctor.id,
            "date": timezone.now(),
            "reason": "Follow-up",
            "status": "Scheduled"
        }
        response = self.client.post(reverse('appointment-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class MedicalRecordTests(APITestSetup):
    def test_get_medical_records(self):
        response = self.client.get(reverse('medicalrecord-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_medical_record(self):
        data = {
            "patient": self.patient.id,
            "doctor": self.doctor.id,
            "diagnosis": "Flu",
            "treatment": "Rest and hydration"
        }
        response = self.client.post(reverse('medicalrecord-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class BillingTests(APITestSetup):
    def test_get_billings(self):
        response = self.client.get(reverse('billing-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_billing(self):
        # Create a new appointment first
        appointment = Appointment.objects.create(
            patient=self.patient,
            doctor=self.doctor,
            date=timezone.now(),
            reason="New checkup",
            status="Scheduled"
        )
        data = {
            "patient": self.patient.id,
            "appointment": appointment.id,
            "amount": 3000,
            "payment_status": "Pending"
        }
        response = self.client.post(reverse('billing-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
