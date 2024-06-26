# Generated by Django 5.0.6 on 2024-05-18 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_pedido_metodo_pagamento_delete_pagamento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('quantidade_estoque', models.PositiveIntegerField(default=0)),
                ('quantidade_minima', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('quantidade_estoque', models.PositiveIntegerField(default=0)),
                ('quantidade_minima', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='itemcardapio',
            name='ingredientes',
        ),
        migrations.AddField(
            model_name='itemcardapio',
            name='produtos',
            field=models.ManyToManyField(to='core.produto'),
        ),
        migrations.AddField(
            model_name='itemcardapio',
            name='ingredientes',
            field=models.ManyToManyField(to='core.ingrediente'),
        ),
    ]
