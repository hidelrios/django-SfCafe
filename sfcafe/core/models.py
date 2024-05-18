import os
import uuid
from django.db import models

# Create your models here.


def get_file_patch(instance, filename):
    ext = filename.split(".")[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('cardapio', filename)


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome


class Ingrediente(models.Model):
    nome = models.CharField(max_length=100)
    quantidade_estoque = models.PositiveIntegerField(default=0)
    quantidade_minima = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nome

    def verificar_estoque(self):
        return self.quantidade_estoque < self.quantidade_minima


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    quantidade_estoque = models.PositiveIntegerField(default=0)
    quantidade_minima = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nome

    def verificar_estoque(self):
        return self.quantidade_estoque < self.quantidade_minima


class ItemCardapio(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    ingredientes = models.ManyToManyField(Ingrediente)
    produtos = models.ManyToManyField(Produto)
    informacoes_nutricionais = models.TextField()
    foto = models.ImageField(upload_to=get_file_patch, blank=True, null=True)

    def __str__(self):
        return self.nome

    def verificar_estoque(self):
        return any(
            ingrediente.verificar_estoque() for ingrediente in self.ingredientes.all()
        ) or any(
            produto.verificar_estoque() for produto in self.produtos.all()
        )


class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    itens = models.ManyToManyField(ItemCardapio, through='ItemPedido')
    data_pedido = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[(
        'PENDENTE', 'Pendente'), ('CONCLUÍDO', 'Concluído')], default='PENDENTE')
    metodo_pagamento = models.CharField(max_length=20, choices=[(
        'DINHEIRO', 'Dinheiro'), ('CARTAO', 'Cartão')], default='DINHEIRO')

    def __str__(self):
        return f"Pedido {self.id} - {self.cliente.nome}"


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    item_cardapio = models.ForeignKey(ItemCardapio, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Item do Pedido {self.pedido.id}: {self.item_cardapio.nome}"
