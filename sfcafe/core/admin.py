from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register([Cliente, ItemCardapio, ItemPedido, Pedido, Pagamento])