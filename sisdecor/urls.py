from django.contrib import admin
from django.urls import path
<<<<<<< HEAD
from home.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    
=======
from calendario.views import CalendarView
from clientes.views import HomeClientes
from home.views import HomeSisDecor

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeSisDecor.as_view(), name='home'),
    path('calendario', CalendarView.as_view(), name='calendario'),
    path('clientes', HomeClientes.as_view(), name='clientes'),
>>>>>>> b19033067acbc30b1c2f27dfcc7c535404402340
]
