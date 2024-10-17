from django import forms
from .models import Venda, VendaDoProduto, Produto

class CriarVendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = []  # Não precisamos de campos adicionais, pois o número da venda é gerado automaticamente


class VendaDoProdutoForm(forms.ModelForm):
    class Meta:
        model = VendaDoProduto
        fields = ['produto', 'qtd']
        labels = {
            'produto': 'Produto',
            'qtd': 'Quantidade',
        }
        widgets = {
            'produto': forms.Select(attrs={'class': 'form-control'}),
            'qtd': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        }
