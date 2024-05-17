from urllib import request
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *

from .models import Cliente, ItemCardapio
from .forms import CardapioForm, ClienteForm


# Create your views here.
def index(request):
    return render(request, 'index.html')

###Cliente
class ClienteListView(ListView):
    model = Cliente
    template_name = 'cliente_list.html'
    context_object_name = 'clientes'

class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'cliente_detail.html'

class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente_form.html'
    success_url = reverse_lazy('cliente-list')

class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente_form.html'
    success_url = reverse_lazy('cliente-list')

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'cliente_confirm_delete.html'
    success_url = reverse_lazy('cliente-list')


###Cardapio
class CardapioListView(ListView):
    model = ItemCardapio
    template_name = 'cardapio_list.html'
    context_object_name = 'itemcardapio'

class CardapioDetailView(DetailView):
    model = ItemCardapio
    template_name = 'cardapio_detail.html'

class CardapioCreateView(CreateView):
    model = ItemCardapio
    form_class = CardapioForm
    template_name = 'cardapio_form.html'
    success_url = reverse_lazy('cardapio-list')

class CardapioUpdateView(UpdateView):
    model = ItemCardapio
    form_class = CardapioForm
    template_name = 'cardapio_form.html'
    success_url = reverse_lazy('cardapio-list')

class CardapioDeleteView(DeleteView):
    model = ItemCardapio
    template_name = 'cardapio_confirm_delete.html'
    success_url = reverse_lazy('cardapio-list')