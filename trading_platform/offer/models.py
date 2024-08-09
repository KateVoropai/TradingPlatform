from django.db import models

from users.models import User
from item.models import Item

class Offer(models.Model):
    """Request to buy or sell specific stocks"""
    BUY = 'buy'
    SELL = 'sell'
    OrderType = [
        (BUY, 'Buy'),
        (SELL, 'Sell'),
    ]
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    item = models.ForeignKey(Item, blank=True, null=True, on_delete=models.SET_NULL)
    entry_quantity = models.IntegerField("Requested quantity")
    quantity = models.IntegerField("Current quantity")
    order_type = models.PositiveSmallIntegerField(choices=OrderType)
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    is_active = models.BooleanField(default=True)
