from django.shortcuts import render
from .models import Doctor, Patient, Appointment, Prescription

def home(request):
    doctors = Doctor.objects.all()
    patients = Patient.objects.all()
    appointments = Appointment.objects.all()
    prescriptions = Prescription.objects.all()

    context = {
        'doctors': doctors,
        'patients': patients,
        'appointments': appointments,
        'prescriptions': prescriptions,
    }

    return render(request, 'home.html', context)