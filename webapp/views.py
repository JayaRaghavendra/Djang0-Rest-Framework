from __future__ import unicode_literals

from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
#from . models import Facility, Floor, Sector
#from . serializers import FacilitySerializer, FloorSerializer, SectorSerializer

# Create your views here.

class FacilityListView(generics.ListCreateAPIView):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer

class FacilityView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FacilitySerializer        
    queryset = Facility.objects.all()

class FloorListView(generics.ListCreateAPIView):
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer

class FloorView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FloorSerializer        
    queryset = Floor.objects.all()

class SecotorListView(generics.ListCreateAPIView):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer

class SecotorView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SectorSerializer
    queryset = Sector.objects.all()


# class FacilityList(APIView):

#     def get(self,request):
#         facility = Facility.objects.all()
#         serializer = FacilitySerializer(facility,many=True)
#         return Response(serializer.data)

#     def post(self):
#         serializer = FacilitySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class FloorList(APIView):

#     def get(self,request,format=None):
#         floor = Floor.objects.all()
#         serializer = FloorSerializer(floor, many=True)
#         return Response(serializer.data)

#     def post(self):
#         pass    

# class SectorList(APIView):
    
#     def get(self,request,format=None):
#         sector = Sector.objects.all()
#         serializer = SectorSerializer(sector, many=True)
#         return Response(serializer.data)

#     def post(self):
#         pass    
# from django.shortcuts import render

# from django.http import HttpResponse
# from django.shortcuts import get_object_or_404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status