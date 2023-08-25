from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .forms import ClienteForm ,EnderecoForm ,OperadorForm ,MaquinaExtrusaoForm ,MaquinaImpressaoForm ,MaquinaCorteForm ,ProdutoForm ,OrdemServicoForm ,TintaForm ,TintaOrdemServicoForm ,IngredientesForm ,IngredienteOrdemServicoForm ,ExtrusaoForm ,ImpressaoForm ,CorteForm
from .models import Cliente, Endereco, Operador, MaquinaExtrusao ,MaquinaImpressao ,MaquinaCorte ,Produto ,OrdemServico ,Tinta ,TintaOrdemServico ,Ingredientes ,IngredienteOrdemServico ,Extrusao ,Impressao ,Corte

