from rest_framework import serializers

from offer.models import Offer


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = [
            "id",
            "user",
            "item",
            "entry_quantity",
            "quantity",
            "order_type",
            "price",
            "is_active",
        ]