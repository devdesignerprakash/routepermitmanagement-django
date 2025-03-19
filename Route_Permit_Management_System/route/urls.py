from django.urls import path
from .views import home_view, vehicle_type_view,vehicle_add_type,editVehicleType,delete_vehicle_type

urlpatterns = [
   path('',home_view, name='home'),
   path('vehicleType/', vehicle_type_view, name="vehicleType"),
   path('add-VehicleType/',vehicle_add_type,name="addVehicleType"),
   path('edit-Vehicle-Type/<int:id>/',editVehicleType,name="editVehicleType"),
   path('delete-vehicle-Type/<int:id>/',delete_vehicle_type,name="deleteVehicleType")
]


