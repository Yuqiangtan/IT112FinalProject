from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('inventory/', views.inventory, name='inventory'),
    path('inventorydetail/<int:id>', views.inventorydetail,name='detail'),
    path('newinventory/',views.newInventory, name='newinventory'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]

