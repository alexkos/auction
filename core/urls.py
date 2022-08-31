from django.urls import path
from django.contrib import admin

from core.views import CreateCatView, LotsAPIView, BetsAPIView, WinBetAPIView


admin.autodiscover()

urlpatterns = [
    path(r'cats/', CreateCatView.as_view(), name='create.cat'),
    path(r'lots/', LotsAPIView.as_view(), name='create.list.lot'),
    path(r'<int:lot_id>/bets/', BetsAPIView.as_view(), name='create.list.bets'),
    path(r'bet/<int:id>', WinBetAPIView.as_view(), name='make.bet.win'),
]