from django.urls import path
from .views import IndexView, NovaVendaView, FinalizarVendaView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('venda', NovaVendaView.as_view(), name='creatvenda'),
    path('venda/finalizar', FinalizarVendaView.as_view(), name='finalizar_venda'),
]
