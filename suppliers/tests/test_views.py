from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import Supplier

class SupplierAPITest(APITestCase):
    def setUp(self):
        Supplier.objects.create(name='Fornecedor A', logo='http://example.com/logo.png', state='São Paulo', cost_per_kwh=0.5, min_kwh_limit=500, total_clients=100, average_rating=4.5)
        Supplier.objects.create(name='Fornecedor B', logo='http://example.com/logo2.png', state='Rio de Janeiro', cost_per_kwh=0.6, min_kwh_limit=300, total_clients=150, average_rating=4.6)

    def test_filter_suppliers(self):
        filter_url = reverse('filter_suppliers')
        data = {'consumption': 400}
        response = self.client.post(filter_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Fornecedor B')

    def test_filter_no_suppliers(self):
        filter_url = reverse('filter_suppliers')
        data = {'consumption': 200}
        response = self.client.post(filter_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['error'], 'Nenhum fornecedor corresponde ao filtro')
