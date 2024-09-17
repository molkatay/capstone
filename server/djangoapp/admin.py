from django.contrib import admin
from .models import CarMake, CarModel

# Register your models here.

# CarModelInline class

# Registering models with their respective admins
admin.site.register(CarMake)
admin.site.register(CarModel)

# Register models here
