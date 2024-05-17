from django import forms
from .models import Cliente, ItemCardapio


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'telefone']


class CardapioForm(forms.ModelForm):
    class Meta:
        model = ItemCardapio
        fields = ['nome', 'descricao', 'preco',
                  'ingredientes', 'informacoes_nutricionais', 'foto']
