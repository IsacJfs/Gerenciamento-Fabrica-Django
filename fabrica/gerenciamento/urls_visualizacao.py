from django.urls import path

from .views_visualizacao import (
    lista_clientes,
    lista_endereco,
    lista_operador,
    lista_maquinas,
    lista_ordens_servico,
    lista_estoques 
)

urlpatterns = [
    path('cliente/', lista_clientes, name='lista_clientes'),

    path('endereco/<int:codigo>/', lista_endereco, name='lista_endereco'),

    path('operador/', lista_operador, name='lista_operador'),

    path('maquinas/', lista_maquinas, name='lista_Maquinas'),

    path('ordens_servico/', lista_ordens_servico, name='lista_ordens_servico'),

    path('estoque/', lista_estoques, name='lista_estoques'),

]