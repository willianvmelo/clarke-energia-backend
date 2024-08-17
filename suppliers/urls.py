from django.urls import path
from .views import SupplierFilterView, SupplierCreateView

urlpatterns = [
    path('filter-suppliers/', SupplierFilterView.as_view(), name='filter_suppliers'),
    path('suppliers/create/', SupplierCreateView.as_view(), name='supplier-create'),
]