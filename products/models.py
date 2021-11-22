from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.TextField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class Budget(models.Model):
    name = models.CharField(max_length=50)
    number = models.DecimalField(max_digits=5, decimal_places=0)
    project = models.CharField(max_length=50)
    client = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Budget_items(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    budget_id = models.ForeignKey(Budget, on_delete=models.DO_NOTHING)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name