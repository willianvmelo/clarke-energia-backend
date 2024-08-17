from django.test import TestCase
from ..models import Supplier
from ..serializers import SupplierSerializer

class SupplierSerializerTest(TestCase):
    def setUp(self):
        self.supplier = Supplier.objects.create(
            name='Fornecedor B',
            logo='http://example.com/logo.png',
            state='Rio de Janeiro',
            cost_per_kwh=0.55,
            min_kwh_limit=600,
            total_clients=200,
            average_rating=4.6
        )
        self.serializer = SupplierSerializer(instance=self.supplier)

    def test_serializer_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'name', 'logo', 'state', 'cost_per_kwh', 'min_kwh_limit', 'total_clients', 'average_rating']))
