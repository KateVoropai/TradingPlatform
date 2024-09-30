from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet

from currency.models import Currency
from currency.serializers import CurrencySerializer


class CurrencyViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
