from typing import Any
from django.http.response import HttpResponse as HttpResponse
from .models import *
from django.views.generic import TemplateView,CreateView,View,ListView,UpdateView,DeleteView
from django.shortcuts import render,redirect,HttpResponse
from django.urls import reverse_lazy
from django.dispatch import receiver
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from decimal import Decimal
from urllib.parse import urlencode
from django.http import HttpRequest
from django.db.models import Q
from .form import *

class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get(self, request):
        return render(request, self.template_name)
    
class NovaVendaView(CreateView):
    template_name = 'creatVenda.html'
    form_class = 