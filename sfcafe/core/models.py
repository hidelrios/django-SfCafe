import os
import uuid
from django.db import models

# Create your models here.

def get_file_patch(instance,filename):
    ext = filename.split(".")[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('cardapio', filename)

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    
    def __str__(self):
        return self.nome
    
class ItemCardapio(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    ingredientes = models.TextField()
    informacoes_nutricionais = models.TextField()
    foto = models.ImageField(upload_to=get_file_patch, blank=True, null=True)
    
    def __str__(self):
        return self.nome
    

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    itens = models.ManyToManyField(ItemCardapio, through='ItemPedido')
    data_pedido = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('PENDENTE', 'Pendente'), ('CONCLUÍDO', 'Concluído')], default='PENDENTE')
    
    def __str__(self):
        return f"Pedido {self.id} - {self.cliente.nome}"
    
    def calcular_subtotal(self):
        total = sum(item.subtotal for item in self.itempedido_set.all())
        self.total = total
        self.save()

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    item_cardapio = models.ForeignKey(ItemCardapio, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    observacoes = models.TextField(blank=True, null=True)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    
    def __str__(self):
        return f"Item do Pedido {self.pedido.id}: {self.item_cardapio.nome}"
    
    def save(self, *args, **kwargs):
        self.subtotal = self.quantidade * self.item_cardapio.preco
        super().save(*args, **kwargs)
        self.pedido.calcular_subtotal()

class Pagamento(models.Model):
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE)
    metodo = models.CharField(max_length=20, choices=[('DINHEIRO', 'Dinheiro'), ('CARTAO', 'Cartão')], default='DINHEIRO')
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    troco = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    data_pagamento = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Pagamento do Pedido {self.pedido.id}"
    
    @property
    def valor_total(self):
        return self.pedido.subtotal + self.troco 

    def save(self, *args, **kwargs):
        self.valor_pago = self.valor_total
        super().save(*args, **kwargs)