from django.contrib import admin
from django.urls import path
from calendario.views import CalendarView
from clientes.views import HomeClientes
from home.views import HomeSisDecor

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeSisDecor.as_view(), name='home'),
    path('calendario', CalendarView.as_view(), name='calendario'),
    path('clientes', HomeClientes.as_view(), name='clientes'),
]
