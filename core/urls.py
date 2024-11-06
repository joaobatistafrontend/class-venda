# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('venda', NovaVendaView.as_view(), name='nova_venda'),
    path('venda/finalizar', FinalizarVendaView.as_view(), name='finalizar_venda'),
    path('venda/diminuir/<int:item_id>', DiminuirQuantidadeEditView.as_view(), name='diminuir_quantidade_edit'),
    path('venda/aumentar/<int:item_id>', AdicionarProdutoEditView.as_view(), name='aumentar_quantidade_edit'),
    path('venda/delete/<int:item_id>', DeleteVenda.as_view(), name='delete_quantidade'),
    path('venda/editar/<int:pk>/', EditarVendaView.as_view(), name='editar_venda'),
    path('venda/editar/<int:venda_pk>/adicionar/', AdicionarProdutoEditView.as_view(), name='adicionar_produto_edit'),
]
