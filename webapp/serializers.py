from rest_framework import serializers, fields
from .models import *
#from . models import Facility, Floor , Sector

class SectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sector
        fields = '__all__'

class FloorSerializer(serializers.ModelSerializer):

    floor_secotrs = SectorSerializer(read_only=True, many=True)    

    class Meta:
        model = Floor
        fields = ('floor_id','floor_no','floor_name','floor_secotrs')

class FacilitySerializer(serializers.ModelSerializer):
    facility_floors = FloorSerializer(read_only=True,many=True) 
    
    class Meta:
        model = Facility
        fields = ('id','Facility_id','name','country','facility_floors')

