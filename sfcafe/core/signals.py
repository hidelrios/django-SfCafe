from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import ItemPedido


@receiver(post_save, sender=ItemPedido)
def atualizar_estoque_apos_adicionar(sender, instance, **kwargs):
    for ingrediente in instance.item_cardapio.ingredientes.all():
        ingrediente.quantidade_estoque -= instance.quantidade
        ingrediente.save()


@receiver(post_delete, sender=ItemPedido)
def atualizar_estoque_apos_remover(sender, instance, **kwargs):
    for ingrediente in instance.item_cardapio.ingredientes.all():
        ingrediente.quantidade_estoque += instance.quantidade
        ingrediente.save()
