from rest_framework import serializers

from watchlist.models import WatchList


class WatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = [
            "id",
            "user",
            "item",
        ]
