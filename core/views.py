from django.shortcuts import render

from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response

from .models import Cat, Lot, Bet
from .serializers import CatSerializer, LotSerializer, BetSerializer, WinBetSerializer


class CreateCatView(generics.ListCreateAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class LotsAPIView(generics.ListCreateAPIView):
    queryset = Lot.objects.all()
    serializer_class = LotSerializer


class BetsAPIView(generics.ListCreateAPIView):
    queryset = Bet.objects.all()
    serializer_class = BetSerializer

    def get_queryset(self):
        lot_id = self.kwargs['lot_id']
        return self.queryset.filter(lot_id=lot_id)


class WinBetAPIView(generics.RetrieveUpdateAPIView):
    queryset = Bet.objects.all()
    serializer_class = WinBetSerializer
    lookup_field = 'id'
