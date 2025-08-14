from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.core.validators import RegexValidator
from django.utils import timezone
from .models import Department, Doctor, Patient, Appointment, MedicalRecord, Billing
from datetime import date

class DepartmentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        max_length=100,
        validators=[
            UniqueValidator(queryset=Department.objects.all()),
            RegexValidator(
                regex=r'^[a-zA-Z ]+$',
                message='Department name must contain only letters and spaces'
            )
        ]
    )

    class Meta:
        model = Department
        fields = ['id', 'name', 'description']
        read_only_fields = ['id']


class DoctorSerializer(serializers.ModelSerializer):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=Doctor.objects.all())]
    )
    phone_number = serializers.CharField(validators=[phone_regex])
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())

    class Meta:
        model = Doctor
        fields = ['id', 'first_name', 'last_name', 'specialization', 'phone_number', 'email', 'department']
        read_only_fields = ['id']


class PatientSerializer(serializers.ModelSerializer):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=Patient.objects.all())]
    )
    phone_number = serializers.CharField(validators=[phone_regex])
    
    def validate_date_of_birth(self, value):
        if value > date.today():
            raise serializers.ValidationError("Date of birth cannot be in the future")
        return value

    class Meta:
        model = Patient
        fields = ['id', 'first_name', 'last_name', 'date_of_birth', 'phone_number', 'email', 'address']
        read_only_fields = ['id']


class AppointmentSerializer(serializers.ModelSerializer):
    def validate_date(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Appointment date cannot be in the past")
        return value

    class Meta:
        model = Appointment
        fields = ['id', 'patient', 'doctor', 'date', 'reason', 'status']
        read_only_fields = ['id']


class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = ['id', 'patient', 'doctor', 'diagnosis', 'treatment', 'created_at']
        read_only_fields = ['id', 'created_at']


class BillingSerializer(serializers.ModelSerializer):
    def validate_amount(self, value):
        if value < 0:
            raise serializers.ValidationError("Amount cannot be negative")
        return value

    class Meta:
        model = Billing
        fields = ['id', 'patient', 'appointment', 'amount', 'payment_status', 'billing_date']
        read_only_fields = ['id', 'billing_date']