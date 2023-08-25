from django.urls import path

from django.urls import path

from .views_visualizacao import (
    lista_clientes,
    lista_operador,
    lista_maquinas,
    lista_ordens_servico,
    lista_estoques 
)

urlpatterns = [
    path('visualizar_cliente/', lista_clientes, name='lista_clientes'),

    path('operador/', lista_operador, name='lista_operador'),

    path('maquina_extrusao/', lista_maquinas, name='lista_Maquinas'),

    path('maquina_impressao/', lista_ordens_servico, name='lista_ordens_servico'),

    path('maquina_corte/', lista_estoques, name='lista_estoques'),

]