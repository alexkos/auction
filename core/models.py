from django.db import models

from users.models import User


class Cat(models.Model):
    breed = models.CharField(max_length=50)
    nickname = models.CharField(max_length=100)
    owner = models.ForeignKey(
        User,
        related_name='cats',
        db_column='owner',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.breed} {self.nickname}'


class Lot(models.Model):
    cat = models.ForeignKey(
        Cat,
        related_name='lots',
        db_column='cat',
        on_delete=models.CASCADE
    )
    price = models.IntegerField()
    owner = models.ForeignKey(
        User,
        related_name='lots',
        db_column='owner',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'Cat {self.cat.nickname} Owner {self.owner.username}'


class Bet(models.Model):
    rate = models.IntegerField()
    owner = models.ForeignKey(
        User,
        related_name='bets',
        db_column='owner',
        on_delete=models.CASCADE
    )
    lot = models.ForeignKey(
        Lot,
        related_name='bets',
        db_column='lot',
        on_delete=models.CASCADE
    )
    win = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.owner.username}'
