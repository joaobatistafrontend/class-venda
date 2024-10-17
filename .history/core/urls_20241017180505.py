from django.urls import path, include
from .views import *
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('venda', NovaVendaView.as_view(*))
]
