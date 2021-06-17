from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('inventory/', views.inventory, name='inventory'),
    path('inventorydetail/<int:id>', views.inventorydetail,name='detail'),
    path('newinventory/',views.newInventory, name='newinventory'),
    path('vehicleType/',views.vehicleType, name='vehicleType'),
    path('rewive/',views.rewive, name='rewive'),
    path('newRewive/',views.newRewive, name='newRewive'),
    path('rewiveDetail/<int:id>',views.rewiveDetail, name='rewiveDetail'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]

