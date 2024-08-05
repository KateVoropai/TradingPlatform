from django.db import models

from currency.models import Currency

class Item(models.Model):
    code = models.CharField("Item Code", max_length=255)
    name = models.CharField("Item Name", max_length=10, unique=True)
    currency = models.ForeignKey(Currency, blank=True, null=True, on_delete=models.SET_NULL)

    

