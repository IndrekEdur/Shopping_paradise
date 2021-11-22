from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    client = models.CharField(max_length=50)

    def __str__(self):
        return self.name