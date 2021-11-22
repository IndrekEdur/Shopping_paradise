from django.db import models
"""
from ...shopping_paradise.projects.models import Project
"""

class Budget(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    client = models.CharField(max_length=50)
    project = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Budget_item(models.Model):
    product = models.CharField(max_length=50)
    product_quantity = models.DecimalField(max_digits=8, decimal_places=2)
    budget = models.ForeignKey(Budget, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.product