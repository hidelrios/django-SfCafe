from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes/', views.ClienteListView.as_view(), name='cliente-list'),
    path('clientes/add/', views.ClienteCreateView.as_view(), name='cliente-add'),
    path('clientes/<int:pk>/', views.ClienteDetailView.as_view(), name='cliente-detail'),
    path('clientes/<int:pk>/edit/', views.ClienteUpdateView.as_view(), name='cliente-edit'),
    path('clientes/<int:pk>/delete/', views.ClienteDeleteView.as_view(), name='cliente-delete'),
]