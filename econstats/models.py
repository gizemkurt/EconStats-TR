from django.db import models


class PriceIndex(models.Model):
    term = models.CharField(max_length=5)
    price_index_rate = models.DecimalField(max_digits=6, decimal_places=4)


class InterestRate(models.Model):
    term = models.CharField(max_length=5)
    interest_rate = models.DecimalField(max_digits=6, decimal_places=4)
