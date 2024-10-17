from django.urls import path
from .views import IndexView, NovaVendaView, FinalizarVendaView, DiminuirQuantidadeView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('venda', NovaVendaView.as_view(), name='nova_venda'),
    path('venda/finalizar', FinalizarVendaView.as_view(), name='finalizar_venda'),
    path('venda/diminuir/<int:item_id>', DiminuirQuantidadeView.as_view(), name='diminuir_quantidade'),
    path('venda/diminuir/<int:item_id>', DiminuirQuantidadeView.as_view(), name='diminuir_quantidade'),
]