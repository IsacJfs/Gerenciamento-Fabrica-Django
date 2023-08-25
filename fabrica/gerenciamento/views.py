from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Cliente, Endereco, Operador, MaquinaExtrusao ,MaquinaImpressao ,MaquinaCorte ,Produto ,OrdemServico ,Tinta ,TintaOrdemServico ,Ingredientes ,IngredienteOrdemServico ,Extrusao ,Impressao ,Corte



def master(request):
    template = loader.get_template('base/master.html')
    return HttpResponse(template.render())

def lista_clientes(request):
    clientes = Cliente.objects.all()
    context = {'clientes': clientes}
    return render(request, 'relatorios/clientes.html', context)

def main(request):
    principal = loader.get_template('main.html')
    return HttpResponse(principal.render())

def testing(request):
    template = loader.get_template('template.html')
    context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
    }
    return HttpResponse(template.render(context, request))