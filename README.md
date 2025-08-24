Hospital Patient Management – Group 10

A Django REST Framework API for managing hospital operations such as doctors, patients, appointments, prescriptions, and billing.

Group Members

| Student ID | Name |
|------------|------|
| 150210     | Erick Githinji |
| 151179     | Abdallah Aymaan Fihri |
| 148831     | Emmanuel Koech |
| 151839     | Serah Wairimu |
| 151956     | Clinton Gikonyo |
| 151104     | Claire Wambui |

Project Overview

The Hospital Patient Management API  allows CRUD operations for managing hospital-related data, including:

- Doctors – Manage doctor details and specializations.
- Patients – Manage patient information.
- Appointments – Schedule and manage patient appointments with doctors.
- Prescriptions – Record medicines prescribed for appointments.
- Bills – Manage hospital billing records.


Models and Relationships

1. Doctor
   - Fields: `name`, `specialization`, `phone`
   - One doctor can have many appointments.

2. Patient
   - Fields: `name`, `age`, `gender`, `phone`
   - One patient can have many appointments.

3. Appointment
   - Fields: `patient`, `doctor`, `date`, `reason`
   - Links `Doctor` and `Patient`.

4. Prescription
   - Fields: `appointment`, `medicine_name`, `dosage`, `instructions`
   - Linked to a specific appointment.

5. Bill
   - Fields: `patient`, `amount`, `date_issued`, `paid`
   - Linked to a specific patient.

Serializers

Each model has its own serializer for:
- Converting model instances to JSON.
- Validating incoming data before saving.

Views / Viewsets

We used ModelViewSet for each model to provide:
- `GET` (list & retrieve)
- `POST` (create)
- `PUT/PATCH` (update)
- `DELETE` (remove)


URL Patterns

The API endpoints are registered via a DRF `DefaultRouter`:

| Endpoint                | Description |
|-------------------------|-------------|
| `/api/doctors/`         | Manage doctors |
| `/api/patients/`        | Manage patients |
| `/api/appointments/`    | Manage appointments |
| `/api/prescriptions/`   | Manage prescriptions |
| `/api/bills/`           | Manage billing |


Testing

We tested endpoints using **Postman** for:
- GET (fetch all / single)
- POST (create new record)
- PUT/PATCH (update record)
- DELETE (remove record)

Example:
```python
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
