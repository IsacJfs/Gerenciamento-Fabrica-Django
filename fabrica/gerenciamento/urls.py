from django.urls import path
from .views import (
    master,
    lista_clientes,
    main,
    testing
)

urlpatterns = [
    path('', master, name='master'),
    path('main', main, name='main'),
    path('testing/', testing, name='testing'),

    path('clientes', lista_clientes, name='lista_clientes'),
]