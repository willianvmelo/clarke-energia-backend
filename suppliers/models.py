from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    logo = models.URLField(max_length=500)
    state = models.CharField(max_length=255)
    cost_per_kwh = models.DecimalField(max_digits=5, decimal_places=2)
    min_kwh_limit = models.PositiveIntegerField()
    total_clients = models.PositiveIntegerField()
    average_rating = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.name
