from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User Model
class CustomUser(AbstractUser):
    is_building_owner = models.BooleanField(default=False)
    is_maintenance_company = models.BooleanField(default=False)
    is_technician = models.BooleanField(default=False)

# Building Owner Model
class BuildingOwner(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username

# Maintenance Company Model
class MaintenanceCompany(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    contact_person = models.CharField(max_length=100)
    company_address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    registration_number = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.user.username

# Technician Model
class Technician(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    company = models.ForeignKey(MaintenanceCompany, on_delete=models.CASCADE)
    specializations = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username

# Building Model
class Building(models.Model):
    owner = models.ForeignKey(BuildingOwner, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Equipment Model
class Equipment(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=50, unique=True)
    equipment_type = models.CharField(max_length=50)  # HVAC, Elevator, etc.
    installation_date = models.DateField()

    def __str__(self):
        return self.name

# Maintenance Job Model
class MaintenanceJob(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    technician = models.ForeignKey(Technician, on_delete=models.CASCADE)
    scheduled_date = models.DateTimeField()
    completion_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('Scheduled', 'Scheduled'), ('In Progress', 'In Progress'), ('Completed', 'Completed')])
    description = models.TextField()

    def __str__(self):
        return f"Job {self.id} - {self.equipment.name}"

# Maintenance Log Model
class MaintenanceLog(models.Model):
    job = models.ForeignKey(MaintenanceJob, on_delete=models.CASCADE)
    technician = models.ForeignKey(Technician, on_delete=models.CASCADE)
    log_date = models.DateTimeField(auto_now_add=True)
    details = models.TextField()

    def __str__(self):
        return f"Log {self.id} for Job {self.job.id}"

