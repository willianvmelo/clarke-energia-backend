from django.test import TestCase
from ..models import Supplier

class SupplierModelTest(TestCase):
    def setUp(self):
        self.supplier = Supplier.objects.create(
            name='Fornecedor A',
            logo='http://example.com/logo.png',
            state='São Paulo',
            cost_per_kwh=0.5,
            min_kwh_limit=500,
            total_clients=100,
            average_rating=4.5
        )

    def test_str_representation(self):
        self.assertEqual(str(self.supplier), 'Fornecedor A')

    def test_supplier_creation(self):
        supplier = Supplier.objects.get(name='Fornecedor A')
        self.assertEqual(supplier.state, 'São Paulo')
        self.assertEqual(supplier.cost_per_kwh, 0.5)
        self.assertEqual(supplier.min_kwh_limit, 500)
        self.assertEqual(supplier.total_clients, 100)
        self.assertEqual(supplier.average_rating, 4.5)
