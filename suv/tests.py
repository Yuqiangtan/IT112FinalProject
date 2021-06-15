from django.test import TestCase
from django.contrib.auth.models import User
from .models import VehicleType, Inventory, Review
import datetime
from .forms import InventoryForm
from django.urls import reverse_lazy, reverse

# Create your tests here.
class VehicleTypeTest(TestCase):
    def setUp(self):
        self.type=VehicleType(typename='SUPERCAR')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'SUPERCAR')

    def test_tablename(self):
        self.assertEqual(str(VehicleType._meta.db_table), 'vehicletype')

class InventoryTest(TestCase):
    def setUp(self):
        self.type=VehicleType(typename='TYPE S')
        self.user=User(username='user1')
        self.inventory=Inventory(inventoryname='PMC Editions', inventorytype=self.type, user=self.user,dateentered=datetime.date(2021,1,20),price=60000.00, inventoryurl='https://www.acura.com/pmc-edition', description="PMC")

    def test_typestring(self):
        self.assertEqual(str(self.inventory),'PMC Editions')

class NewInventoryForm(TestCase):
    #valid form data
    def test_inventoryform(self):
        data={
                'inventoryname':'2021 Acura RDX PMC Editions', 
                'inventorytype':'Suv',
                'user':'yuqiang',
                'dateentered':'2021-6-15',
                'price':'60000.00',
                'inventoryurl':'https://www.acura.com/rdx',
                'description':'The RDX offers a 272-HP86 turbocharged 2.0-liter engine and available Super Handling All-Wheel Drive™ (SH-AWD®). The most sophisticated SH-AWD system yet, the torque-vectoring all-wheel drive system delivers more accurate handling for all road conditions'
            }
        form=InventoryForm (data)
        self.assertTrue(form.is_valid)

class New_Inventory_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testuser1',password='sql12345')
        self.type=VehicleType.objects.create(typename='car')
        self.inventory=Inventory.objects.create(inventoryname='PMC Editions', inventorytype=self.type, user=self.test_user,dateentered=datetime.date(2021,1,20),price=600.00, inventoryurl='https://www.acura.com/pmc-edition', description="PMC")

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newinventory'))
        self.assertRedirects(response, '/accounts/login/?next=/suv/newinventory/')