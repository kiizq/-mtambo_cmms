from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-building/', views.add_building, name='add_building'),
    path('add-equipment/<int:building_id>/', views.add_equipment, name='add_equipment'),
    path('add-job/', views.add_job, name='add_job'),
]
