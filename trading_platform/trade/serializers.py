from rest_framework import serializers

from trade.models import Trade


class TradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = [
            "id",
            "item",
            "seller",
            "buyer",
            "quantity",
            "unit_price",
            "description",
            "buyer_offer",
            "seller_offer",
        ]