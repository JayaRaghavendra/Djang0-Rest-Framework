from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Facility(models.Model):
    #facility fields
    Facility_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=10)
    location = models.CharField(max_length=10)
    city = models.CharField(max_length=10)
    country = models.CharField(max_length=10)

    def __str__(self):
        return self.Facility_id
  
class Floor(models.Model):
    #ForeignKey
    facility_id = models.ForeignKey(Facility, on_delete=models.CASCADE,related_name='facility_floors',null=True, blank=True)
    #floor fields
    floor_id = models.CharField(max_length=10, unique=True)
    floor_no = models.IntegerField()
    floor_name = models.CharField(max_length=10)

class Sector(models.Model):
     #ForeignKey
     floorid = models.ForeignKey(Floor,on_delete=models.CASCADE,related_name='floor_secotrs',null=True, blank=True)
     #sector fields
     sectorid = models.IntegerField()
     sectorname = models.CharField(max_length=15)

