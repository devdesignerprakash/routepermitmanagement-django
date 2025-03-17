from django.db import models

# Create your models here.

class VehicleType(models.Model):
    type= models.CharField(max_length=50) 
    def __str__(self):
        return self.type

class Route(models.Model):
       route=models.CharField(max_length=1000)
       def __str__(self):
            return self.route
       
class YatayatSewa(models.Model):
        name=models.CharField(max_length=200)
        address=models.CharField(max_length=200)
        registeredDate= models.DateField()
        expiryDate= models.DateField()
        def __str__(self):
            return self.name
        
class Vehicle(models.Model):
        type=models.ForeignKey(VehicleType, on_delete=models.CASCADE)
        ijajat_no=models.CharField(max_length=50, unique=True)
        vehicle_no= models.CharField(max_length=100)
        yatayat_sewa=models.ForeignKey(YatayatSewa,on_delete=models.CASCADE,null=True)
        chassis_no= models.CharField(max_length=100)
        vehicleOwner=models.CharField(max_length=200,default="Ram")
        engine_no= models.CharField(max_length=100)
        insuranceDate=models.DateField()
        vehicleFitnessTestDate=models.DateField()
        rajaswo=models.DecimalField(max_digits=10,decimal_places=2, default=0.00)
        issueDate=models.DateField(auto_now=True)
        expiryDate=models.DateField()
        isRouteChange=models.BooleanField(default=False)
        isRenew=models.BooleanField(default=False)
        route=models.ForeignKey(Route,on_delete=models.CASCADE)
        def __str__(self):
            return self.vehicle_no
        






       
    
