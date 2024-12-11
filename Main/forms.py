from django import forms
from .models import *

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointments
        fields = "__all__"

class MechanicsForm(forms.ModelForm):
    class Meta:
        model = Mechanics
        fields = "__all__"