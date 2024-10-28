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
        venda_id = request.session.get('venda_id')
        venda = None
        produtos_adicionados = []

        if venda_id:
            venda = get_object_or_404(Venda, id=venda_id)
            produtos_adicionados = venda.itens.all()
        
        # Recupera todos os produtos para exibição no formulário
        produtos = Produto.objects.all()

        context = {
            'venda': venda,
            'produtos': produtos,
            'produtos_adicionados': produtos_adicionados,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        venda_id = request.session.get('venda_id')

        if not venda_id:
            venda = Venda.objects.create()
            request.session['venda_id'] = venda.id
        else:
            venda = get_object_or_404(Venda, id=venda_id)

        produto_id = request.POST.get('produto_id')
        produto = get_object_or_404(Produto, id=produto_id)

        # Verifica se o produto já está na venda
        item_venda, created = VendaDoProduto.objects.get_or_create(
            venda=venda, produto=produto, qtd=1
        )
        if not created:
            # Se já existir, aumenta a quantidade
            item_venda.qtd += 1
        item_venda.save()

        return redirect('nova_venda')
    
class FinalizarVendaView(View):
    def get(self, request):
        venda_id = request.session.get('venda_id')
        
        if not venda_id:
            messages.error(request, "Nenhuma venda em andamento para finalizar.")
            return redirect('creatvenda')

        # Recupera a venda e os itens associados
        venda = get_object_or_404(Venda, id=venda_id)
        produtos_adicionados = venda.itens.all()
        
        if not produtos_adicionados:
            messages.error(request, "Adicione produtos à venda antes de finalizar.")
            return redirect('creatvenda')

        # Aqui você pode realizar ações adicionais, como salvar um status de finalizado para a venda.
        venda.finalizada = True  # Supondo que tenha um campo para marcar como finalizada
        venda.save()

        # Limpa a sessão da venda para permitir uma nova
        del request.session['venda_id']

        messages.success(request, "Venda finalizada com sucesso!")
        return redirect('index')
    

class DiminuirQuantidadeView(View):
    def post(self, request, item_id):
        item_venda = get_object_or_404(VendaDoProduto, id=item_id)

        # Diminui a quantidade, mas garante que não fique abaixo de 1
        if item_venda.qtd > 1:
            item_venda.qtd -= 1
            item_venda.save()
        elif
        else:
            messages.error(request, "A quantidade mínima é 1.")

        return redirect('nova_venda')

class AumentarQuantidadeView(View):
    def post(self, request, item_id):
        item_venda = get_object_or_404(VendaDoProduto, id=item_id)
        
        # Aumenta a quantidade do produto em 1
        item_venda.qtd += 1
        item_venda.save()
        
        return redirect('nova_venda')
