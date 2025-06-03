from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name

class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
        ('U', 'Unknown'),  # Add an unknown option

    ]
    
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,default='U')
    contact_number = models.CharField(max_length=15,blank=True, null=True)
    
    def __str__(self):
        return self.name

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('C', 'Completed'),
        ('X', 'Cancelled'),
    ]
    
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    
    def __str__(self):
        return f"{self.patient.name} with Dr. {self.doctor.name} on {self.date}"