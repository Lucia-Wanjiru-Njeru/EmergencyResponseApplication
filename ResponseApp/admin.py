from django.contrib import admin
from .models import *  # Import all models from the current directory

# Register your models here.

admin.site.register(Coordinates)
admin.site.register(FireResources)
admin.site.register(MedicalResourses)
admin.site.register(PoliceResources)