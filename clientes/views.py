from django.shortcuts import render
from django.views.generic.base import TemplateView

class  HomeClientes(TemplateView):
    template_name = "clientes.html"