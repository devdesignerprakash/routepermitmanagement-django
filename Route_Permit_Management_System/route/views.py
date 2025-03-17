from django.shortcuts import render,redirect
from .models import*

# Create your views here.
def home_view(request):
    return render(request,"homePage.html") 

def vehicle_type_view(request):
      totalVehicleTypes= VehicleType.objects.all()
      context={
           "vehicleTypes":totalVehicleTypes
      }
      return render(request,"vehicleType.html",context)
def vehicle_add_type(request):
    if request.method == "POST":
        vehicle_type = request.POST.get("type")
        if vehicle_type:
            VehicleType.objects.create(type=vehicle_type)
            
        return redirect("vehicleType")  
    return render(request, "vehicleType.html")

def editVehicleType(request,id):
    
    vehicle = VehicleType.objects.get(id=id)
    print(vehicle)
    context={
        "vehicleType":vehicle
    }
    if request.method == "POST":
        vehicle.type = request.POST.get("type")
        vehicle.save()
        return redirect('vehicleType')
    return render(request, 'vehicleType.html',context)



        
