from django.db import models

class Car(models.Model):

#    TRANSMISSION = {
   #     ('Manuel', 'Manuel'),
    #    ('AUTOMATIQUE', 'AUTOMATIQUE'),
    #}
    carMake = models.CharField(max_length=100,default='')
    carModel = models.CharField(max_length=100,blank=True) 
    carMileage = models.IntegerField(default=0)
    carColor = models.CharField(max_length=20,default='')
    carTransmission = models.CharField(max_length=30,default='')
    carYear=models.IntegerField(default='')
    carCylinders = models.CharField(max_length=20,blank=True)
    carEngine = models.IntegerField(default='')
    carFuel = models.CharField(max_length=100,default='')
    carPrice = models.IntegerField(default=0)
    link= models.CharField(max_length=1000,default='', blank=True, null=True)
    img=models.URLField(blank=True,null=True)
    def __str__(self):
        return self.carMake
        