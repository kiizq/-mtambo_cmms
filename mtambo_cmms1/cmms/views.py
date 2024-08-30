from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Building, Equipment, MaintenanceJob, Technician
from .forms import BuildingForm, EquipmentForm, MaintenanceJobForm

@login_required
def dashboard(request):
    if request.user.is_building_owner:
        buildings = Building.objects.filter(owner=request.user.buildingowner)
        return render(request, 'cmms/building_owner_dashboard.html', {'buildings': buildings})
    elif request.user.is_maintenance_company:
        jobs = MaintenanceJob.objects.filter(technician__company=request.user.maintenancecompany)
        return render(request, 'cmms/maintenance_company_dashboard.html', {'jobs': jobs})
    elif request.user.is_technician:
        jobs = MaintenanceJob.objects.filter(technician=request.user.technician)
        return render(request, 'cmms/technician_dashboard.html', {'jobs': jobs})

@login_required
def add_building(request):
    if request.method == 'POST':
        form = BuildingForm(request.POST)
        if form.is_valid():
            building = form.save(commit=False)
            building.owner = request.user.buildingowner
            building.save()
            return redirect('dashboard')
    else:
        form = BuildingForm()
    return render(request, 'cmms/add_building.html', {'form': form})

@login_required
def add_equipment(request, building_id):
    building = get_object_or_404(Building, id=building_id)
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            equipment = form.save(commit=False)
            equipment.building = building
            equipment.save()
            return redirect('dashboard')
    else:
        form = EquipmentForm()
    return render(request, 'cmms/add_equipment.html', {'form': form})

@login_required
def add_job(request):
    if request.method == 'POST':
        form = MaintenanceJobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = MaintenanceJobForm()
    return render(request, 'cmms/add_job.html', {'form': form})

