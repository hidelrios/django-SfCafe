from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import ItemPedido, Ingrediente, Produto


@receiver(post_save, sender=ItemPedido)
def atualizar_estoque_apos_adicionar(sender, instance, **kwargs):
    for ingrediente in instance.item_cardapio.ingredientes.all():
        ingrediente.quantidade_estoque -= instance.quantidade
        ingrediente.save()
    for produto in instance.item_cardapio.produtos.all():
        produto.quantidade_estoque -= instance.quantidade
        produto.save()


@receiver(post_delete, sender=ItemPedido)
def atualizar_estoque_apos_remover(sender, instance, **kwargs):
    for ingrediente in instance.item_cardapio.ingredientes.all():
        ingrediente.quantidade_estoque += instance.quantidade
        ingrediente.save()
    for produto in instance.item_cardapio.produtos.all():
        produto.quantidade_estoque += instance.quantidade
        produto.save()
