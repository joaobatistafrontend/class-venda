from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('venda', NovaVendaView.as_view(), name='nova_venda'),
    path('venda/finalizar', FinalizarVendaView.as_view(), name='finalizar_venda'),
    path('venda/diminuir/<int:item_id>', DiminuirQuantidadeView.as_view(), name='diminuir_quantidade'),
    path('venda/aumentar/<int:item_id>', AumentarQuantidadeView.as_view(), name='aumentar_quantidade'),
    path('venda/delete/<int:item_id>', DeleteVenda.as_view(), name='delete_quantidade'),

        path('editar_venda/<int:pk>/', EditarVendaView.as_view(), name='editar_venda'),

]
