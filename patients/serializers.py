from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Department, Doctor, Patient, Appointment, MedicalRecord, Billing


class DepartmentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        max_length=100,
        validators=[UniqueValidator(queryset=Department.objects.all(), message="Department name must be unique.")]
    )

    class Meta:
        model = Department
        fields = ['id', 'name', 'description']
        read_only_fields = ['id']


class DoctorSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=Doctor.objects.all(), message="Doctor email must be unique.")]
    )
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())

    class Meta:
        model = Doctor
        fields = ['id', 'first_name', 'last_name', 'specialization', 'phone_number', 'email', 'department']
        read_only_fields = ['id']


class PatientSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=Patient.objects.all(), message="Patient email must be unique.")]
    )

    class Meta:
        model = Patient
        fields = ['id', 'first_name', 'last_name', 'date_of_birth', 'phone_number', 'email', 'address']
        read_only_fields = ['id']


class AppointmentSerializer(serializers.ModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())
    doctor = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all())

    class Meta:
        model = Appointment
        fields = ['id', 'patient', 'doctor', 'date', 'reason', 'status']
        read_only_fields = ['id']


class MedicalRecordSerializer(serializers.ModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())
    doctor = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all(), allow_null=True, required=False)

    class Meta:
        model = MedicalRecord
        fields = ['id', 'patient', 'doctor', 'diagnosis', 'treatment', 'created_at']
        read_only_fields = ['id', 'created_at']


class BillingSerializer(serializers.ModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())
    appointment = serializers.PrimaryKeyRelatedField(queryset=Appointment.objects.all())

    class Meta:
        model = Billing
        fields = ['id', 'patient', 'appointment', 'amount', 'payment_status', 'billing_date']
        read_only_fields = ['id', 'billing_date']
