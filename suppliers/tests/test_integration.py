from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class SupplierIntegrationTest(APITestCase):
    def test_create_and_filter_supplier(self):
        
        supplier_data = {
            'name': 'Fornecedor C',
            'logo': 'http://example.com/logo.png',
            'state': 'Minas Gerais',
            'cost_per_kwh': 0.6,
            'min_kwh_limit': 400,
            'total_clients': 150,
            'average_rating': 4.7
        }
        response = self.client.post(reverse('supplier_create'), supplier_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        filter_url = reverse('filter_suppliers')
        data = {'consumption': 500}
        response = self.client.post(filter_url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Fornecedor C')
