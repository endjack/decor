from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.decorators.csrf import csrf_exempt
from eventos.models import *

@csrf_exempt
def home(request):
    template_name = "home.html"
    eventos = Evento.objects.all()
    return render(request, template_name=template_name, context={'eventos': eventos})