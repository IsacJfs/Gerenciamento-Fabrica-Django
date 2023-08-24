from django.urls import path
from . import views
from .views import (
    master,
    lista_clientes,
    main,
    cliente_view,
    operador_view,
    maquina_extrusao_view,
    maquina_impressao_view,
    maquina_corte_view,
    produto_view,
    ordem_servico_view,
    tinta_view,
    ingredientes_view,
    extrusao_view,
    impressao_view,
    corte_view,
    testing
)

urlpatterns = [
    path('', master, name='master'),
    path('main', main, name='main'),
    path('adicionar_cliente/', cliente_view, name='cliente_create'),
    path('testing/', testing, name='testing'),

    path('clientes', lista_clientes, name='lista_clientes'),

    path('operador/', operador_view, name='operador_create'),
    path('operador/<int:id>/', operador_view, name='operador_update'),

    path('maquina_extrusao/', maquina_extrusao_view, name='maquina_extrusao_create'),
    path('maquina_extrusao/<int:id>/', maquina_extrusao_view, name='maquina_extrusao_update'),

    path('maquina_impressao/', maquina_impressao_view, name='maquina_impressao_create'),
    path('maquina_impressao/<int:id>/', maquina_impressao_view, name='maquina_impressao_update'),

    path('maquina_corte/', maquina_corte_view, name='maquina_corte_create'),
    path('maquina_corte/<int:id>/', maquina_corte_view, name='maquina_corte_update'),

    path('produto/', produto_view, name='produto_create'),
    path('produto/<int:id>/', produto_view, name='produto_update'),

    path('ordem_servico/', ordem_servico_view, name='ordem_servico_create'),
    path('ordem_servico/<int:id>/', ordem_servico_view, name='ordem_servico_update'),

    path('tinta/', tinta_view, name='tinta_create'),
    path('tinta/<int:id>/', tinta_view, name='tinta_update'),

    path('ingredientes/', ingredientes_view, name='ingredientes_create'),
    path('ingredientes/<int:id>/', ingredientes_view, name='ingredientes_update'),

    path('extrusao/', extrusao_view, name='extrusao_create'),
    path('extrusao/<int:id>/', extrusao_view, name='extrusao_update'),

    path('impressao/', impressao_view, name='impressao_create'),
    path('impressao/<int:id>/', impressao_view, name='impressao_update'),

    path('corte/', corte_view, name='corte_create'),
    path('corte/<int:id>/', corte_view, name='corte_update'),
]