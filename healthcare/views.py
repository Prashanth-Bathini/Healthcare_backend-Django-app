# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import api_view  # Add this import
from rest_framework.response import Response  # Add this import
from rest_framework.reverse import reverse  # Add this import
from .models import Doctor, Patient, Appointment
from .serializers import DoctorSerializer, PatientSerializer, AppointmentSerializer

# Add this new view function at the top of the class definitions
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'doctors': reverse('doctor-list', request=request, format=format),
        'patients': reverse('patient-list', request=request, format=format),
        'appointments': reverse('appointment-list', request=request, format=format),
        'admin': request.build_absolute_uri('/admin/')  # Special case for admin
    })

# Your existing view classes below
class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer