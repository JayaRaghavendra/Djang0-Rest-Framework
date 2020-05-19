from django.test import TestCase
from webapp.models import *

#Inorder to run this code >> python manage.py test webapp.tests

# Create your tests here.
class FacilityTestCase(TestCase):

    def setUp(self):

        print("Facility Setup activity")

        #creating 2 records to  check database functionality
        Facility.objects.create(Facility_id = "BDC",
                                name = "Amazon",
                                location = "Electronic City",
                                city = "Bangalore",
                                country = "India") #record1
        Facility.objects.create(Facility_id = "HDC",
                                name = "Apple",
                                location = "Hitech City",
                                city = "Hyderabad",
                                country = "India") #record2

    def test_facility_info(self):

        print("Testing Facility Information")

        qs = Facility.objects.all()
        #checking our database with our input records by their count
        self.assertEqual(qs.count(),2) #condition to compare whehter the created records 2 or not

        f1 = Facility.objects.get(Facility_id = "BDC") #getting reference object from record 1 
        f2 = Facility.objects.get(Facility_id = "HDC") #getting reference object from record 2
        
        self.assertEqual(f1.get_Facilityname(),"Amazon") #checking particular data info with their respected record
        self.assertEqual(f2.get_Facilityname(),"Apple")

class FloorTestCase(TestCase):
    
    def setUp(self):

        print("Floor Setup activity")

        #creating 2 records to  check database functionality

        Floor.objects.create(floor_id = "F1003",
                            floor_no = 1,
                            floor_name = "Jame bond") #record1

        Floor.objects.create(floor_id = "F1004",
                            floor_no = 2,
                            floor_name = "Jack Sparrow") #record2

    def test_floor_info(self):

        print("Testing Floor Information")

        qs = Floor.objects.all()
        #checking our database with our input records by their count
        self.assertGreater(qs.count(),1) #condition to compare whehter the created records Grater than the value

        fl_1 = Floor.objects.get(floor_no = 1) #getting reference object from record 1 
        fl_2 = Floor.objects.get(floor_no = 2) #getting reference object from record 2
        
        self.assertEqual(fl_1.get_Floor_id(),"F1003") #checking particular data info with their respected record
        self.assertEqual(fl_2.get_Floor_id(),"F1004") 

class SectorTestCase(TestCase):
    
    def setUp(self):

        print("Sector Setup activity")

        #creating 3 records to  check database functionality

        Sector.objects.create(sectorid = 7,
                            sectorname = "Mahatma Gandhi") #record1

        Sector.objects.create(sectorid = 8,
                            sectorname = "Alluri Sita Rama Raju") #record2

        Sector.objects.create(sectorid = 9,
                            sectorname = "Komaram Bheem") #record3                  

    def test_floor_info(self):

        print("Testing Sector Information")

        qs = Sector.objects.all()
        #checking our database with our input records by their count
        self.assertNotEqual(qs.count(),2) #condition to compare whehter the created records

        s1 = Sector.objects.get(sectorname = "Mahatma Gandhi") #getting reference object from record 1 
        s2 = Sector.objects.get(sectorname = "Alluri Sita Rama Raju") #getting reference object from record 2
        s3 = Sector.objects.get(sectorname = "Komaram Bheem") #getting reference object from record 3
        
        self.assertEqual(s1.get_sectorid(),7) #checking particular data info with their respected record
        self.assertEqual(s2.get_sectorid(),8)                
        self.assertEqual(s3.get_sectorid(),9)                



