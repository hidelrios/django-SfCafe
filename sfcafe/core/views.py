from urllib import request
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import *
from django.db.models import F
from .models import Cliente, Ingrediente, ItemCardapio, ItemPedido, Pedido
from .forms import CardapioForm, ClienteForm, IngredienteForm, ItemPedidoForm, ItemPedidoFormSet, PedidoForm



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

###Pedido
class PedidoCreateView(CreateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'pedido_form.html'
    success_url = reverse_lazy('pedido-list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['itens'] = ItemPedidoFormSet(self.request.POST)
        else:
            data['itens'] = ItemPedidoFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        itens = context['itens']
        self.object = form.save()
        if itens.is_valid():
            itens.instance = self.object
            itens.save()
        return super().form_valid(form)
    

class PedidoListView(ListView):
    model = Pedido
    template_name = 'pedido_list.html'
    context_object_name = 'pedidos'

class PedidoDetailView(DetailView):
    model = Pedido
    template_name = 'pedido_detail.html'

class PedidoUpdateView(UpdateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'pedido_form.html'
    success_url = reverse_lazy('pedido-list')

class PedidoDeleteView(DeleteView):
    model = Pedido
    template_name = 'pedido_confirm_delete.html'
    success_url = reverse_lazy('pedido-list')


def adicionar_item_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    if request.method == 'POST':
        form = ItemPedidoForm(request.POST)
        if form.is_valid():
            item_pedido = form.save(commit=False)
            item_pedido.pedido = pedido
            item_pedido.save()
            return redirect('pedido-detail', pk=pedido_id)
    else:
        form = ItemPedidoForm()
    
    return render(request, 'adicionar_item_pedido.html', {'form': form, 'pedido': pedido})

def deletar_item_pedido(request, pedido_id, item_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    item_pedido = get_object_or_404(ItemPedido, id=item_id)
    item_pedido.delete()
    return redirect('pedido-detail', pk=pedido_id)


def editar_item_pedido(request, pedido_id, item_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    item_pedido = get_object_or_404(ItemPedido, id=item_id)
    
    if request.method == 'POST':
        form = ItemPedidoForm(request.POST, instance=item_pedido)
        if form.is_valid():
            form.save()
            return redirect('pedido-detail', pk=pedido_id)
    else:
        form = ItemPedidoForm(instance=item_pedido)
    
    return render(request, 'editar_item_pedido.html', {'form': form, 'pedido': pedido})

######Ingredientes e Produtos
class IngredienteListView(ListView):
    model = Ingrediente
    template_name = 'ingrediente_list.html'
    context_object_name = 'ingredientes'

class IngredienteDetailView(DetailView):
    model = Ingrediente
    template_name = 'ingrediente_detail.html'

class IngredienteCreateView(CreateView):
    model = Ingrediente
    form_class = IngredienteForm
    template_name = 'ingrediente_form.html'
    success_url = reverse_lazy('ingrediente-list')

class IngredienteUpdateView(UpdateView):
    model = Ingrediente
    form_class = IngredienteForm
    template_name = 'ingrediente_form.html'
    success_url = reverse_lazy('ingrediente-list')

class IngredienteDeleteView(DeleteView):
    model = Ingrediente
    template_name = 'ingrediente_confirm_delete.html'
    success_url = reverse_lazy('ingrediente-list')


def alerta_reposicao(request):
    ingredientes = Ingrediente.objects.filter(quantidade_estoque__lte=F('quantidade_minima'))
    return render(request, 'alerta_reposicao.html', {'ingredientes': ingredientes})
