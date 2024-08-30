from django import forms
from .models import Building, Equipment, MaintenanceJob, Technician

class BuildingForm(forms.ModelForm):
    class Meta:
        model = Building
        fields = ['name', 'address']

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['name', 'serial_number', 'equipment_type', 'installation_date']

class MaintenanceJobForm(forms.ModelForm):
    class Meta:
        model = MaintenanceJob
        fields = ['equipment', 'technician', 'scheduled_date', 'description']

class TechnicianForm(forms.ModelForm):
    class Meta:
        model = Technician
        fields = ['company', 'specializations']
