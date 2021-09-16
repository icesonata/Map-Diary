from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Memory

# Register your models here.
@admin.register(Memory)
class MemoryManager(OSMGeoAdmin):
    model = Memory