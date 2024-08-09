from django.db import models

from item.models import Item

class Price(models.Model):
    """Item prices"""
    item = models.ForeignKey(Item, blank=True, null=True, on_delete=models.CASCADE, related_name='prices', related_query_name='prices')
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    date = models.DateField(unique=True, blank=True, null=True)
