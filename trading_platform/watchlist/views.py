from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet

from watchlist.models import WatchList
from watchlist.serializers import WatchlistSerializer


class WatchlistViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = WatchList.objects.all()
    serializer_class = WatchlistSerializer


