from rest_framework.test import APITestCase
from webapp.models import *

        #inorder to run this you need to run
        #python manage.py test Myproject.tests

class FacilityTestCase(APITestCase):
    def setUp(self):
        Facility.objects.create(Facility_id = "BDC1",
                                name = "Amazon",
                                location = "E City",
                                city = "Bangalore",
                                country = "India")
    def test_get_method(self):
        url = 'http://127.0.0.1:8000/api/facility/'
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        qs = Facility.objects.filter(name = 'Amazon')
        self.assertEqual(qs.count(),1)
        print("Facility GET Method status code:",response.status_code)

    def test_post_method_success(self):
        url = 'http://127.0.0.1:8000/api/facility/'
        data = {
        "Facility_id": "BDC4",
        "name": "Jaya Tech",
        "location": "Tech Street",
        "city": "Bangalore",
        "country": "India",
        }
        response = self.client.post(url,data,format='json')
        print(response.status_code)
        self.assertEqual(response.status_code, 201)
        print("Facility POST Method status code for Success:",response.status_code)

    def test_post_method_fail(self):
        url = 'http://127.0.0.1:8000/api/facility/'
        data = {
        "Facility_id": "BDC1",
        "name": "Jaya Tech",
        "country": "India",
        }
        response = self.client.post(url,data,format='json')
        print(response.status_code)
        self.assertEqual(response.status_code, 400) 
        print("Facility POST Method status code for Fail:",response.status_code)

    def test_delete_method_Success(self):
        url = 'http://127.0.0.1:8000/api/facility/1/'
        
        response = self.client.delete(url)
        print(response.status_code)
        self.assertEqual(response.status_code, 204) 
        print("Facility DELETE Method status code for Success:",response.status_code)

class FloorTestCase(APITestCase):
    def setUp(self):
        Floor.objects.create(floor_id = "F1003",
                            floor_no = 2,
                            floor_name = "Jame bond")
    def test_get_method(self):
        url = 'http://127.0.0.1:8000/api/floor/'
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        qs = Floor.objects.filter(floor_name = 'Jame bond')
        self.assertEqual(qs.count(),1)
        print("Floor GET Method status code:",response.status_code)

    def test_post_method_success(self):
        url = 'http://127.0.0.1:8000/api/floor/'
        data = {
        "floor_id": "F1009",
        "floor_no": 2,
        "floor_name": "James bond"
        }
        response = self.client.post(url,data,format='json')
        print(response.status_code)
        self.assertEqual(response.status_code, 201)
        print("Floor POST Method status code for Success:",response.status_code)

    def test_post_method_fail(self):
        url = 'http://127.0.0.1:8000/api/floor/'
        data = {
        "floor_no": 2,
        "floor_name": "James bond"
        }
        response = self.client.post(url,data,format='json')
        print(response.status_code)
        self.assertEqual(response.status_code, 400) 
        print("Floor POST Method status code for Fail:",response.status_code) 

    def test_delete_method_Success(self):
        url = 'http://127.0.0.1:8000/api/floor/1/'
        response = self.client.delete(url)
        print(response.status_code)
        self.assertEqual(response.status_code, 204) 
        print("Floor DELETE Method status code for Success:",response.status_code)

class SectorTestCase(APITestCase):
    def setUp(self):
        Sector.objects.create(sectorid = 7,
                            sectorname = "Howard stark")
    def test_get_method(self):
        url = 'http://127.0.0.1:8000/api/sector/'
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        qs = Sector.objects.filter(sectorname = 'Howard stark')
        self.assertEqual(qs.count(),1)
        print("Sector GET Method status code:",response.status_code)

    def test_post_method_success(self):
        url = 'http://127.0.0.1:8000/api/sector/'
        data = {
        "sectorid": 9,
        "sectorname": "IRON MAN"
        }
        response = self.client.post(url,data,format='json')
        print(response.status_code)
        self.assertEqual(response.status_code, 201)
        print("Sector POST Method status code for Success:",response.status_code)

    def test_post_method_fail(self):
        url = 'http://127.0.0.1:8000/api/sector/'
        data = {
        "sectorname": "IRON MAN"
        }
        response = self.client.post(url,data,format='json')
        print(response.status_code)
        self.assertEqual(response.status_code, 400) 
        print("Sector POST Method status code for Fail:",response.status_code) 

    def test_delete_method_Success(self):
        url = 'http://127.0.0.1:8000/api/sector/1/'
        response = self.client.delete(url)
        print(response.status_code)
        self.assertEqual(response.status_code, 204) 
        print("Sector DELETE Method status code for Success:",response.status_code)