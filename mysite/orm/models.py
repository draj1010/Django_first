from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    name = models.CharField(max_length=200)
    customer = models.ManyToManyField(Customer,related_name="vehicle")

    def __str__(self):
        return self.name