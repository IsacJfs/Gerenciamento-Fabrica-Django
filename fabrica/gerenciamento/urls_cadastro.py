from django.urls import path

from .views_cadastro import (
    cliente_add,
    operador_add,
    maquina_extrusao_add,
    maquina_impressao_add,
    maquina_corte_add,
    produto_add,
    ordem_servico_add,
    tinta_add,
    ingredientes_add,
    extrusao_add,
    impressao_add,
    corte_add,
    ingrediente_produto_add,
    produtos_por_ordem,
    extrusao_form_add,
    get_produtos,
    get_ingredientes
)

urlpatterns = [
    path('adicionar_cliente/', cliente_add, name='cliente_create'),
    path('adicionar_cliente/<int:id>/', cliente_add, name='cliente_update'),

    path('operador/', operador_add, name='operador_create'),
    path('operador/<int:id>/', operador_add, name='operador_update'),

    path('maquina_extrusao/', maquina_extrusao_add, name='maquina_extrusao_create'),
    path('maquina_extrusao/<int:id>/', maquina_extrusao_add, name='maquina_extrusao_update'),

    path('maquina_impressao/', maquina_impressao_add, name='maquina_impressao_create'),
    path('maquina_impressao/<int:id>/', maquina_impressao_add, name='maquina_impressao_update'),

    path('maquina_corte/', maquina_corte_add, name='maquina_corte_create'),
    path('maquina_corte/<int:id>/', maquina_corte_add, name='maquina_corte_update'),

    path('produto/', produto_add, name='produto_create'),
    path('produto/<int:id>/', produto_add, name='produto_update'),

    path('ordem_servico/', ordem_servico_add, name='ordem_servico_create'),
    path('ordem_servico/<int:id>/', ordem_servico_add, name='ordem_servico_update'),

    path('tinta/', tinta_add, name='tinta_create'),
    path('tinta/<int:id>/', tinta_add, name='tinta_update'),

    path('ingredientes/', ingredientes_add, name='ingredientes_create'),
    path('ingredientes/<int:id>/', ingredientes_add, name='ingredientes_update'),

    path('ingrediente_produto/', ingrediente_produto_add, name='ingrediente_produto_create'),

    path('extrusao/', extrusao_add, name='extrusao_create'),
    path('extrusao/<int:id>/', extrusao_add, name='extrusao_update'),

    path('impressao/', impressao_add, name='impressao_create'),
    path('impressao/<int:id>/', impressao_add, name='impressao_update'),

    path('corte/', corte_add, name='corte_create'),
    path('corte/<int:id>/', corte_add, name='corte_update'),

    path('api/produtos_por_ordem/<int:ordem_id>/', produtos_por_ordem, name='produtos_por_ordem'),

    path('formulario_extrusao/', extrusao_form_add, name='formulario_extrusao'),
    
    path('get_produtos/', get_produtos, name='get_produtos'),

    path('get_ingredientes/', get_ingredientes, name='get_ingredientes'),
]