from rest_framework import serializers

from core.models import Cat, Lot, Bet


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = '__all__'


class LotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lot
        fields = '__all__'


class BetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bet
        fields = '__all__'
    #TODO validate case when user owner of lot


class WinBetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bet
        fields = ['win']
