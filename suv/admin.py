from django.contrib import admin
from .models import VehicleType, Inventory, Review
# Register your models here.
admin.site.register(VehicleType)
admin.site.register(Inventory)
admin.site.register(Review)