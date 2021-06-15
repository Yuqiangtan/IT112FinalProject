from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class VehicleType(models.Model):
    typename=models.CharField(max_length=255)
    typedescription=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.typename

    class Meta:
        db_table='vehicletype'

class Inventory(models.Model):
    inventoryname=models.CharField(max_length=255)
    inventorytype=models.ForeignKey(VehicleType, on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    dateentered=models.DateField()
    price=models.DecimalField(max_digits=8,decimal_places=2)
    inventoryurl=models.URLField()
    description=models.TextField()

    def __str__(self):
        return self.inventoryname

    class Meta:
        db_table='inventory'

class Review(models.Model):
    title=models.CharField(max_length=255)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    inventory=models.ForeignKey(Inventory, on_delete=models.CASCADE)
    reviewdate=models.DateField()
    reviewtext=models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        db_table='review'