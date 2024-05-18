from django import forms
from .models import Cliente, Ingrediente, ItemCardapio, ItemPedido, Pedido

from django.forms import inlineformset_factory



class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'telefone']


class CardapioForm(forms.ModelForm):
    class Meta:
        model = ItemCardapio
        fields = ['nome', 'descricao', 'preco',
                  'ingredientes', 'informacoes_nutricionais', 'foto']


class ItemPedidoForm(forms.ModelForm):
    class Meta:
        model = ItemPedido
        fields = ['item_cardapio', 'quantidade', 'observacoes']

class PedidoForm(forms.ModelForm):
    itens = forms.inlineformset_factory(Pedido, ItemPedido, form=ItemPedidoForm, extra=1)

    class Meta:
        model = Pedido
        fields = ['cliente','status','metodo_pagamento']

ItemPedidoFormSet = inlineformset_factory(Pedido, ItemPedido, form=ItemPedidoForm, extra=1, can_delete=True)

class IngredienteForm(forms.ModelForm):
    class Meta:
        model= Ingrediente
        fields = "__all__"