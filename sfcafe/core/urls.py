from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes/', views.ClienteListView.as_view(), name='cliente-list'),
    path('clientes/add/', views.ClienteCreateView.as_view(), name='cliente-add'),
    path('clientes/<int:pk>/', views.ClienteDetailView.as_view(),
         name='cliente-detail'),
    path('clientes/<int:pk>/edit/',
         views.ClienteUpdateView.as_view(), name='cliente-edit'),
    path('clientes/<int:pk>/delete/',
         views.ClienteDeleteView.as_view(), name='cliente-delete'),

    path('cardapio/', views.CardapioListView.as_view(), name='cardapio-list'),
    path('cardapio/add/', views.CardapioCreateView.as_view(), name='cardapio-add'),
    path('cardapio/<int:pk>/', views.CardapioDetailView.as_view(),
         name='cardapio-detail'),
    path('cardapio/<int:pk>/edit/',
         views.CardapioUpdateView.as_view(), name='cardapio-edit'),
    path('cardapio/<int:pk>/delete/',
         views.CardapioDeleteView.as_view(), name='cardapio-delete'),

    path('pedido/', views.PedidoListView.as_view(), name='pedido-list'),
    path('pedido/add', views.PedidoCreateView.as_view(), name='pedido-add'),
    path('pedido/<int:pk>/', views.PedidoDetailView.as_view(), name='pedido-detail'),
    path('pedido/<int:pk>/edit/',
         views.PedidoUpdateView.as_view(), name='pedido-edit'),
    path('pedido/<int:pk>/delete/',
         views.PedidoDeleteView.as_view(), name='pedido-delete'),
    path('pedido/<int:pedido_id>/adicionar-item/', 
         views.adicionar_item_pedido, name='pedido-adicionar-item'),
    path('pedido/<int:pedido_id>/editar-item/<int:item_id>/',
         views.editar_item_pedido, name='pedido-editar-item'),
    path('pedido/<int:pedido_id>/deletar-item/<int:item_id>/',
         views.deletar_item_pedido, name='item-delete'),



]
