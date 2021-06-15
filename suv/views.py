from django.shortcuts import render
from .models import Inventory, VehicleType, Review
# Create your views here.
def index(request):
    return render(request,'suv/index.html')

def inventory(request):
    inventory_list=Inventory.objects.all()
    return render(request,'suv/inventory.html',{'inventory_list':inventory_list})