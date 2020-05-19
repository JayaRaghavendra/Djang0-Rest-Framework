from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Facility(models.Model):
    #facility fields
    Facility_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)

    def get_Facilityname(self):
        return self.name
  
class Floor(models.Model):
    #ForeignKey
    facility_id = models.ForeignKey(Facility, on_delete=models.CASCADE,related_name='facility_floors',null=True, blank=True)
    #floor fields
    floor_id = models.CharField(max_length=10, unique=True)
    floor_no = models.IntegerField()
    floor_name = models.CharField(max_length=20)
    
    def get_Floor_id(self):
        return self.floor_id
        
class Sector(models.Model):
     #ForeignKey
     floorid = models.ForeignKey(Floor,on_delete=models.CASCADE,related_name='floor_secotrs',null=True, blank=True)
     #sector fields
     sectorid = models.IntegerField()
     sectorname = models.CharField(max_length=20)

     def get_sectorid(self):
         return self.sectorid

