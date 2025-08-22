from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Tariff(models.Model):
    name = models.CharField(max_length=100)
    price_per_kwh = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class UsageRecord(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    tariff = models.ForeignKey(Tariff, on_delete=models.CASCADE)
    kwh_used = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
