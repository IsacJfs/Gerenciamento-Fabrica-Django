from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .forms import (ClienteForm,
        EnderecoForm,
        OperadorForm,
        MaquinaExtrusaoForm,
        MaquinaImpressaoForm,
        MaquinaCorteForm,
        ProdutoForm,
        OrdemServicoForm,
        TintaForm,
        TintaOrdemServicoForm,
        IngredientesForm,
        IngredienteOrdemServicoForm,
        ExtrusaoForm,
        ImpressaoForm,
        CorteForm,
        AcabamentoForm,
        TratamentoForm,
        MaterialForm,
        CorForm)
from .models import (
        Cliente,
        Endereco,
        Operador,
        MaquinaExtrusao,
        MaquinaImpressao,
        MaquinaCorte,
        Tratamento,
        Material,
        Acabamento,
        CorProduto,
        Produto,
        OrdemServico,
        StatusServico,
        Tinta,
        TintaOrdemServico,
        Ingredientes,
        IngredienteOrdemServico,
        Extrusao,
        Impressao,
        Corte,
        ProdutoExtrusao,
        ProdutoImpressao,
        ProdutoCorte
        )

def cliente_add(request):
    form = ClienteForm(request.POST or None)
    endereco_form = EnderecoForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid() and endereco_form.is_valid():
            cliente = form.save() # Save the Cliente instance first.
            
            endereco = endereco_form.save(commit=False) # Don't save the Endereco instance yet.
            endereco.cliente = cliente # Associate the saved Cliente instance with the Endereco instance.
            endereco.save() # Now save the Endereco instance.
            
            return redirect('#')

    return render(request, 'add/adicionar_cliente.html', {'form': form, 'endereco_form': endereco_form })

def operador_add(request, id=None):
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
    return render(request, 'add/operador.html', context)

def maquina_extrusao_add(request):
    if request.method == 'POST':
        form = MaquinaExtrusaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alguma_url')
    else:
        form = MaquinaExtrusaoForm()
    return render(request, 'add/maquina_extrusao.html', {'form': form})

def maquina_impressao_add(request):
    if request.method == 'POST':
        form = MaquinaImpressaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alguma_url')
    else:
        form = MaquinaImpressaoForm()
    return render(request, 'add/maquina_impressao.html', {'form': form})

def maquina_corte_add(request):
    if request.method == 'POST':
        form = MaquinaCorteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alguma_url')
    else:
        form = MaquinaCorteForm()
    return render(request, 'add/maquina_corte.html', {'form': form})

def produto_add_old(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/produtos')
    else:
        form = ProdutoForm()
    return render(request, 'add/produto.html', {'form': form})

def produto_add(request):
    if request.method == 'POST':
        produto_form = ProdutoForm(request.POST)
        if produto_form.is_valid():
            produto_form.save()
            return redirect('../visualizacao/produtos')  # Substitua pelo nome da URL de destino
    else:
        produto_form = ProdutoForm()

    return render(request, 'add/produto.html', {'produto_form': produto_form})

def ordem_servico_add(request):
    if request.method == 'POST':
        produto_form = ProdutoForm(request.POST or None)
        ordem_form = OrdemServicoForm(request.POST or None)
        if produto_form.is_valid():
            produto = produto_form.save()

            ordem = ordem_form.save(commit=False)
            ordem.produto = produto
            ordem.save()

            return redirect('../visualizacao/ordens_servico')  # Substitua pelo nome da URL de destino
    else:
        ordem_form = OrdemServicoForm()
        produto_form = ProdutoForm()

    return render(request, 'add/ordem_servico.html', {'ordem_form': ordem_form, 'produto_form': produto_form})

def ordem_servico_add_old(request):
    ordem_form = OrdemServicoForm(request.POST or None)
    produto_form = ProdutoForm(request.POST or None)

    if request.method == 'POST':
        if ordem_form.is_valid() and produto_form.is_valid():
            cliente = ordem_form.save() # Save the Cliente instance first.
            
            produto = produto_form.save(commit=False) # Don't save the produto instance yet.
            produto.cliente = cliente # Associate the saved Cliente instance with the produto instance.
            produto.save() # Now save the Endereco instance.
            
            return redirect('#')

    return render(request, 'add/ordem_servico.html', {'ordem_form': ordem_form, 'produto_form': produto_form })

def tinta_add(request):
    if request.method == 'POST':
        form = TintaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alguma_url')
    else:
        form = TintaForm()
    return render(request, 'add/tinta.html', {'form': form})

def ingredientes_add(request):
    if request.method == 'POST':
        form = IngredientesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alguma_url')
    else:
        form = IngredientesForm()
    return render(request, 'add/ingredientes.html', {'form': form})

def extrusao_add(request):
    if request.method == 'POST':
        form = ExtrusaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alguma_url')
    else:
        form = ExtrusaoForm()
    return render(request, 'seu_template.html', {'form': form})

def impressao_add(request):
    if request.method == 'POST':
        form = ImpressaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alguma_url')
    else:
        form = ImpressaoForm()
    return render(request, 'seu_template.html', {'form': form})

def corte_add(request):
    if request.method == 'POST':
        form = CorteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alguma_url')
    else:
        form = CorteForm()
    return render(request, 'seu_template.html', {'form': form})


# -------------- Fim views de cadastro ------------------------


