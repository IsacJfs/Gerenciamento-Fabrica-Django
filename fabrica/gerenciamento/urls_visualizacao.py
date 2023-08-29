from django.urls import path

from .views_visualizacao import (
    lista_clientes,
    lista_endereco,
    lista_operador,
    lista_maquinas,
    lista_ordens_servico,
    lista_estoques,
    lista_produtos,
    lista_extrusao 
)

urlpatterns = [
    path('cliente/', lista_clientes, name='lista_clientes'),

    path('produtos/', lista_produtos, name='lista_produtos'),

    path('endereco/<int:codigo>/', lista_endereco, name='lista_endereco'),

    path('operador/', lista_operador, name='lista_operador'),

    path('maquinas/', lista_maquinas, name='lista_Maquinas'),

    path('ordens_servico/', lista_ordens_servico, name='lista_ordens_servico'),

    path('estoque/', lista_estoques, name='lista_estoques'),

    path('lista_extrusao/', lista_extrusao, name='lista_extrusao'),

]