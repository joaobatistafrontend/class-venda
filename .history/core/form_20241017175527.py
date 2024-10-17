from django import forms
from .models import *


class CriarVenda(forms.Form):
    class Meta:
        model = 