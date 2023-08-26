from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .forms import ClienteForm ,EnderecoForm ,OperadorForm ,MaquinaExtrusaoForm ,MaquinaImpressaoForm ,MaquinaCorteForm ,ProdutoForm ,OrdemServicoForm ,TintaForm ,TintaOrdemServicoForm ,IngredientesForm ,IngredienteOrdemServicoForm ,ExtrusaoForm ,ImpressaoForm ,CorteForm
from .models import Cliente, Endereco, Operador, MaquinaExtrusao ,MaquinaImpressao ,MaquinaCorte ,Produto ,OrdemServico ,Tinta ,TintaOrdemServico ,Ingredientes ,IngredienteOrdemServico ,Extrusao ,Impressao ,Corte

def lista_clientes(request):
    cliente = Cliente.objects.prefetch_related('endereco_set').all()
    context = {'cliente': cliente}
    return render(request, 'visualizacao/cliente.html', context)

def lista_produtos(request):
    produto = Produto.objects.select_related('cor_produto', 'acabamento_produto', 'tratamento_produto', 'material_produto').all()
    context = {'produtos': produto}
    return render(request, 'visualizacao/produtos.html', context)

def lista_endereco(request, codigo):
    cliente = Cliente.objects.get(codigo=codigo)
    endereco = Endereco.objects.get(cliente=cliente)
    
    context = {'endereco': endereco}
    return render(request, 'visualizacao/cliente.html', context)

def lista_operador(request):
    operador = Operador.objects.all()
    context = {'operador': operador}
    return render(request, 'visualizacao/operador.html', context)

def lista_maquinas(request):
    extrusao = MaquinaExtrusao.objects.all()
    corte = MaquinaCorte.objects.all()
    impressao = MaquinaImpressao.objects.all()
    context = {'extrusao': extrusao, 'corte': corte, 'impressao': impressao}
    return render(request, 'visualizacao/maquinas.html', context)

def lista_ordens_servico(request):
    ordem_servico = OrdemServico.objects.all()
    context = {'ordem_servico': ordem_servico}
    return render(request, 'visualizacao/ordem_servico.html', context)

def lista_estoques(request):
    estoques = Cliente.objects.all()
    context = {'estoques': estoques}
    return render(request, 'visualizacao/estoques.html', context)

