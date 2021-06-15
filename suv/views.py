from django.shortcuts import render,get_object_or_404
from .models import Inventory, VehicleType, Review
from django.urls import reverse_lazy
# Create your views here.
def index(request):
    return render(request,'suv/index.html')

def inventory(request):
    inventory_list=Inventory.objects.all()
    return render(request,'suv/inventory.html',{'inventory_list':inventory_list})

def inventorydetail(request,id):
    inventory=get_object_or_404(Inventory,pk=id)
    return render(request,'suv/inventorydetail.html',{'inventory':inventory})