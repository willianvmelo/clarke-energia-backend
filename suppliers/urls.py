from django.urls import path
from .views import SupplierFilterView

urlpatterns = [
    path('filter-suppliers/', SupplierFilterView.as_view(), name='filter_suppliers'),
]