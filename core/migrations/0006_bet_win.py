# Generated by Django 4.1 on 2022-08-31 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_lot_winner'),
    ]

    operations = [
        migrations.AddField(
            model_name='bet',
            name='win',
            field=models.BooleanField(default=False),
        ),
    ]