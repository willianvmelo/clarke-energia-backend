from django.contrib import admin
from .models import Supplier

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'state', 'cost_per_kwh', 'min_kwh_limit', 'total_clients', 'average_rating')