from django.contrib import admin
from django.urls import path
from clientes.views import HomeClientes
from home.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('clientes', HomeClientes.as_view(), name='clientes'),
]

