from django.contrib import admin
from .models import Department, Doctor, Patient, Appointment, MedicalRecord, Billing

admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(MedicalRecord)
admin.site.register(Billing)
