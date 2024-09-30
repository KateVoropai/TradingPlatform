from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet

from trade.models import Trade
from trade.serializers import TradeSerializer
from trade.tasks import add
from trading_platform.celery import debug_task


class TradeViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer

    add.delay(2, 3)
    debug_task.delay()
