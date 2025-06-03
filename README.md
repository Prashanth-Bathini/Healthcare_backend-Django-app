Healthcare Backend Assignment
Overview
Django REST API for patient-doctor management with JWT authentication. Manages healthcare records through secure RESTful endpoints.

Core Features
✅ User registration/login with JWT

✅ Patient & doctor CRUD operations

✅ Secure doctor-patient assignments

✅ PostgreSQL database integration

Key Endpoints
Auth: /register/, /login/

Patients: /patients/, /patients/{id}/

Doctors: /doctors/

Assignments: /assign-doctor/

Setup
Clone repo and install requirements

Configure PostgreSQL in .env

Run python manage.py runserver

Access API at: http://localhost:8000/

