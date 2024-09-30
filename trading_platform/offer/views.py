from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet

from offer.models import Offer
from offer.serializers import OfferSerializer


class OfferViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

