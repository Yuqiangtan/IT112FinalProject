from django import forms
from .models import VehicleType, Inventory, Review

class InventoryForm(forms.ModelForm):
    class Meta:
        model=Inventory
        fields='__all__'