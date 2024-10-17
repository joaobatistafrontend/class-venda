from typing import Any
from django.http import HttpResponse
from .models import *
from django.views.generic import TemplateView, CreateView, View, ListView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from decimal import Decimal
from .form import CriarVendaForm, VendaDoProdutoForm
from django.forms import modelformset_factory



class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get(self, request):
        return render(request, self.template_name)
    
class NovaVendaView(View):
    template_name = 'createVenda.html'

    def get(self, request):
        produtos = Produto.objects.all()
        venda_id = request.session.get('venda_id')

        # Verifica se já existe uma venda em andamento
        venda = None
        if venda_id:
            venda = get_object_or_404(Venda, id=venda_id)
            produtos_adicionados = venda.itens.all()
        else:
            produtos_adicionados = []

        return render(request, self.template_name, {
            'produtos': produtos,
            'produtos_adicionados': produtos_adicionados,
        })

    def post(self, request):
        produto_id = request.POST.get('produto_id')

        # Recupera ou cria uma nova venda
        venda_id = request.session.get('venda_id')
        if venda_id:
            venda = get_object_or_404(Venda, id=venda_id)
        else:
            venda = Venda.objects.create()
            request.session['venda_id'] = venda.id

        # Adiciona o produto à venda
        produto = get_object_or_404(Produto, id=produto_id)
        venda_produto = VendaDoProduto.objects.create(
            venda=venda,
            produto=produto,
            qtd=1  # Quantidade inicial, pode ser ajustado conforme necessário
        )
        venda_produto.save()

        messages.success(request, f'Produto {produto.nome} adicionado à venda!')

        return redirect('nova_venda')  # Ajuste a URL conforme necessário