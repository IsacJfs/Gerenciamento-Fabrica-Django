from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .forms import ClienteForm ,EnderecoForm ,OperadorForm ,MaquinaExtrusaoForm ,MaquinaImpressaoForm ,MaquinaCorteForm ,ProdutoForm ,OrdemServicoForm ,TintaForm ,TintaOrdemServicoForm ,IngredientesForm ,IngredienteOrdemServicoForm ,ExtrusaoForm ,ImpressaoForm ,CorteForm
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

def cliente_view(request):
    form = ClienteForm()
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        endereco_form = EnderecoForm(request.POST)
        if form.is_valid() and endereco_form.is_valid():
            endereco = endereco_form.save()
            cliente = form.save(commit=False)
            cliente.endereco = endereco
            cliente.save()
            return redirect('/clientes')
    else:
        form = ClienteForm()
        endereco_form = EnderecoForm()

    return render(request, 'addCliente', {'form': form, 'endereco_form': endereco_form})

def operador_view(request, id=None):
    if id:
        instance = get_object_or_404(Operador, id=id)
        form = OperadorForm(request.POST or None, instance=instance)
    else:
        form = OperadorForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('url_para_lista_de_operadores')

    context = {'form': form}
    return render(request, 'operador_template.html', context)

def maquina_extrusao_view(request):
    if request.method == 'POST':
        form = MaquinaExtrusaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alguma_url')
    else:
        form = MaquinaExtrusaoForm()
    return render(request, 'seu_template.html', {'form': form})

def maquina_impressao_view(request):
    if request.method == 'POST':
        form = MaquinaImpressaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alguma_url')
    else:
        form = MaquinaImpressaoForm()
    return render(request, 'seu_template.html', {'form': form})

def maquina_corte_view(request):
    if request.method == 'POST':
        form = MaquinaCorteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alguma_url')
    else:
        form = MaquinaCorteForm()
    return render(request, 'seu_template.html', {'form': form})

def produto_view(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alguma_url')
    else:
        form = ProdutoForm()
    return render(request, 'seu_template.html', {'form': form})

def ordem_servico_view(request):
    if request.method == 'POST':
        form = OrdemServicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alguma_url')
    else:
        form = OrdemServicoForm()
    return render(request, 'seu_template.html', {'form': form})

def tinta_view(request):
    if request.method == 'POST':
        form = TintaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alguma_url')
    else:
        form = TintaForm()
    return render(request, 'seu_template.html', {'form': form})

def ingredientes_view(request):
    if request.method == 'POST':
        form = IngredientesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alguma_url')
    else:
        form = IngredientesForm()
    return render(request, 'seu_template.html', {'form': form})

def extrusao_view(request):
    if request.method == 'POST':
        form = ExtrusaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alguma_url')
    else:
        form = ExtrusaoForm()
    return render(request, 'seu_template.html', {'form': form})

def impressao_view(request):
    if request.method == 'POST':
        form = ImpressaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alguma_url')
    else:
        form = ImpressaoForm()
    return render(request, 'seu_template.html', {'form': form})

def corte_view(request):
    if request.method == 'POST':
        form = CorteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alguma_url')
    else:
        form = CorteForm()
    return render(request, 'seu_template.html', {'form': form})