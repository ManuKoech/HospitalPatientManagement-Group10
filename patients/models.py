from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone

# -----------------------
# Department Model
# -----------------------
class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


# -----------------------
# Doctor Model
# -----------------------
class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    specialization = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="doctors")

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name}"


# -----------------------
# Patient Model
# -----------------------
class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# -----------------------
# Appointment Model
# -----------------------
class Appointment(models.Model):
    STATUS_CHOICES = [
        ("Scheduled", "Scheduled"),
        ("Completed", "Completed"),
        ("Cancelled", "Cancelled"),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="appointments")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="appointments")
    date = models.DateTimeField()
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Scheduled")

    def __str__(self):
        return f"Appointment with {self.doctor} for {self.patient} on {self.date}"


# -----------------------
# Medical Record Model
# -----------------------
class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="medical_records")
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, related_name="medical_records")
    diagnosis = models.TextField()
    treatment = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Medical Record for {self.patient} ({self.created_at.date()})"


# -----------------------
# Billing Model
# -----------------------
class Billing(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Paid", "Paid"),
        ("Cancelled", "Cancelled"),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="billings")
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE, related_name="billing")
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default="Pending")
    billing_date = models.DateTimeField(default=timezone.now)

    def __str__(self):

        return f"Bill for {self.patient} - {self.amount} ({self.payment_status})"
