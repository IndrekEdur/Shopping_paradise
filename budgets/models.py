from django.db import models

from projects.models import Project

class Budget(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    client = models.CharField(max_length=50)
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

class Budget_item(models.Model):
    product = models.CharField(max_length=50)
    product_quantity = models.DecimalField(default=1, max_digits=8, decimal_places=0)
    budget = models.ForeignKey(Budget, on_delete=models.DO_NOTHING)
    product_price = models.DecimalField(default=1, max_digits=8, decimal_places=2)

    def calc_total(self):
        amount = (self.product_price * self.product_quantity)
        return amount

    def __str__(self):
        return self.product