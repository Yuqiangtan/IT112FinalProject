from django import forms
from .models import VehicleType, Inventory, Review

class InventoryForm(forms.ModelForm):
    class Meta:
        model=Inventory
        fields='__all__'

class VehicleType(forms.ModelForm):
    class Meta:
        model = VehicleType
        fields = '__all__'

class Review(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'