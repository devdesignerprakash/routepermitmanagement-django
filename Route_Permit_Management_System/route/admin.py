from django.contrib import admin
from .models import Vehicle, VehicleType, Route,YatayatSewa
# Register your models here.

admin.site.register(VehicleType)
admin.site.register(Vehicle)
admin.site.register(Route)
admin.site.register(YatayatSewa)

