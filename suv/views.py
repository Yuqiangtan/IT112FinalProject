from django.shortcuts import render,get_object_or_404
from .models import Inventory, VehicleType, Review
from django.urls import reverse_lazy
from .forms import InventoryForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request,'suv/index.html')

def inventory(request):
    inventory_list=Inventory.objects.all()
    return render(request,'suv/inventory.html',{'inventory_list':inventory_list})

def inventorydetail(request,id):
    inventory=get_object_or_404(Inventory,pk=id)
    return render(request,'suv/inventorydetail.html',{'inventory':inventory})

def vehicleType(request):
    vehicle_type=VehicleType.objects.all()
    return render(request,'suv/vehicletype.html',{'vehicle_type':vehicle_type})

def review(request):
    review=Review.objects.values('id', 'title')
    return render(request,'suv/review.html',{'review':review})

def reviewDetails(request, id):
    details = get_object_or_404(Review, pk=id)
    return render(request, 'club/reviewDetails.html', {"details": details})

@login_required
def newInventory(request):
    form=InventoryForm

    if request.method=='POST':
        form=InventoryForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=InventoryForm()
    else:
        form=InventoryForm()
    return render(request,'suv/newinventory.html',{'form':form})

def loginmessage(request):
    return render(request, 'suv/loginmessage.html')

def logoutmessage(request):
    return render(request, 'suv/logoutmessage.html')