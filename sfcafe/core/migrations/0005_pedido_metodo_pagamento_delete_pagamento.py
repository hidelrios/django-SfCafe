# Generated by Django 5.0.6 on 2024-05-18 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_itempedido_subtotal_remove_pedido_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='metodo_pagamento',
            field=models.CharField(choices=[('DINHEIRO', 'Dinheiro'), ('CARTAO', 'Cartão')], default='DINHEIRO', max_length=20),
        ),
        migrations.DeleteModel(
            name='Pagamento',
        ),
    ]
