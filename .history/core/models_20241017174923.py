from django.db import models
from django.db.models import Max
from decimal import Decimal
from django.db.models.signals import pre_save
from django.dispatch import receiver
from datetime import date
from django.utils import timezone


class NovaCategoria(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self) -> str:
        return f'{self.nome}'


class Produto(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tipo_categoria = models.ForeignKey(NovaCategoria, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} x {self.valor}"  


class Venda(models.Model):
    numero_venda = models.IntegerField()
    data_venda = models.DateField(default=date.today)

    def __str__(self):
        return f"Venda #{self.numero_venda} - {self.data_venda}"
    


class VendaDoProduto(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, related_name='itens', blank=True, null=True)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    qtd = models.IntegerField(blank=True, null=True)
    
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"Venda {self.venda} - Produto {self.produto.nome} - {self.qtd} unidades - Total: R${self.total} - Data {self.data_venda}"



# Função que será chamada antes de salvar uma instância de VendaDoProduto
@receiver(pre_save, sender=VendaDoProduto)
def update_total(sender, instance, **kwargs):
    # Verifica se o produto e a quantidade não são nulos e calcula o total
    if instance.produto.valor and instance.qtd:
        instance.total = instance.produto.valor * instance.qtd
    else:
        instance.total = 0  # Define total como 0 se valor ou qtd forem nulos
