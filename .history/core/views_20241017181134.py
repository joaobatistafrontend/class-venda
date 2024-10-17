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
    
class NovaVendaView(CreateView):
    template_name = 'createVenda.html'
    form_class = CriarVendaForm  # Formulário para criar a venda
    success_url = reverse_lazy('index')  # Redireciona para o index após salvar a venda

    def get(self, request):
        venda_form = self.form_class()
        produto_form = VendaDoProdutoForm()
        return render(request, self.template_name, {
            'venda_form': venda_form,
            'produto_form': produto_form,
        })

    def post(self, request):
        venda_form = self.form_class(request.POST)
        ProdutoFormSet = modelformset_factory(VendaDoProduto, form=VendaDoProdutoForm, extra=3)
        formset = ProdutoFormSet(request.POST)

        if venda_form.is_valid() and formset.is_valid():
            # Salva a nova venda
            nova_venda = venda_form.save()

            # Salva cada produto associado à venda
            for form in formset:
                produto_venda = form.save(commit=False)
                produto_venda.venda = nova_venda  # Associa o produto à venda recém-criada
                produto_venda.save()

            messages.success(request, 'Venda e produtos adicionados com sucesso!')
            return redirect(self.success_url)
        else:
            # Renderiza novamente o formulário em caso de erro
            return render(request, self.template_name, {
                'venda_form': venda_form,
                'formset': formset,
            })