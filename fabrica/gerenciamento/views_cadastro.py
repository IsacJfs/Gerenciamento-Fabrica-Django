from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404
from django.core.serializers import serialize
from django.utils import timezone
from django.urls import reverse
from django.http import JsonResponse
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
        CorForm,
        ExtrusaoUpdateForm)
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
            
            return redirect('../cliente')

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
            return redirect('../produtos')  # Substitua pelo nome da URL de destino
    else:
        produto_form = ProdutoForm()

    return render(request, 'add/produto.html', {'produto_form': produto_form})

ProdutoFormSet = inlineformset_factory(OrdemServico, Produto, form=ProdutoForm, extra=1)

def ordem_servico_add(request):
    if request.method == 'POST':
        ordem_form = OrdemServicoForm(request.POST)
        produto_formset = ProdutoFormSet(request.POST, instance=OrdemServico())
        
        if ordem_form.is_valid() and produto_formset.is_valid():
            ordem_servico = ordem_form.save()
            produtos = produto_formset.save(commit=False)
            for produto in produtos:
                produto.ordem_servico = ordem_servico
                produto.save()
            for produto in produto_formset.deleted_objects:
                produto.delete()
            return redirect('../ordens_servico')
    else:
        ordem_form = OrdemServicoForm()
        produto_formset = ProdutoFormSet(instance=OrdemServico())
        
    return render(request, 'add/ordem_servico.html', {'ordem_form': ordem_form, 'produto_formset': produto_formset})


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

def ingrediente_produto_add(request):
    ordens = OrdemServico.objects.all()
    produtos = Produto.objects.none()
    form = IngredienteOrdemServicoForm()

    if request.method == 'POST':
        # Obter os valores dos campos 'ingrediente' e 'qtde' de todos os formulários
        ingredientes = request.POST.getlist('ingrediente')
        qtde = request.POST.getlist('qtde')

        # Obter os IDs da ordem de serviço e do produto selecionados
        ordem_id = request.POST.get('ordem_servico')
        produto_id = request.POST.get('produto')

        # Obter os objetos da ordem de serviço e do produto
        ordem = OrdemServico.objects.get(id=ordem_id)
        produto = Produto.objects.get(id=produto_id)

        # Iterar sobre todos os formulários de ingredientes e criar novos objetos IngredienteOrdemServico
        for i in range(len(ingredientes)):
            IngredienteOrdemServico.objects.create(
                ingrediente_id=ingredientes[i],
                qtde=qtde[i],
                ordemservico=ordem,
                produto=produto
            )

        return redirect('/main')

    return render(request, 'add/ingrediente_produto.html', {
        'form': form,
        'ordens': ordens,
        'produtos': produtos,
    })

def produtos_por_ordem(request, ordem_id):
    produtos = list(Produto.objects.filter(ordem_servico_id=ordem_id).values('id', 'tipo'))
    return JsonResponse(produtos, safe=False)

def extrusao_form_add(request):
    if request.method == 'POST':
        form = ExtrusaoForm(request.POST)
        if form.is_valid():
            form.save()

            # Obter os IDs de OrdemServico e Produto do campo produto_ingrediente
            ordem_servico_id = form.cleaned_data['produto_ingrediente'].ordemservico.id
            produto_id = form.cleaned_data['produto_ingrediente'].produto.id

            # Construir a URL de redirecionamento com os parâmetros de consulta
            redirect_url = reverse('ingredientes_extrusao')
            params = f'?ordem_servico_id={ordem_servico_id}&produto_id={produto_id}'
            full_url = f'{redirect_url}{params}'

            return redirect(full_url)
        else:
            print(form.errors)
    else:
        form = ExtrusaoForm()

    return render(request, 'add/formulario_extrusao.html', {'form': form})

def get_produtos(request):
    ordem_servico_id = request.GET.get('ordem_servico')
    produtos = Produto.objects.filter(ordem_servico_id=ordem_servico_id)
    produto_list = list(produtos.values('id', 'tipo'))
    return JsonResponse({'produtos': produto_list})

def extrusao_form_add_old(request):
    if request.method == 'POST':
        produto_form = ExtrusaoForm(request.POST)
        if produto_form.is_valid():
            produto_form.save()
            return redirect('../produtos')  # Substitua pelo nome da URL de destino
    else:
        produto_form = ExtrusaoForm()

    return render(request, 'add/formulario_extrusao.html', {'produto_form': produto_form})

def ingredientes_por_produto(request, produto_id):
    ingredientes = IngredienteOrdemServico.objects.filter(ordemservico_id=produto_id).values('ingrediente', 'qtde')
    ingredientes_list = list(ingredientes)
    return JsonResponse({'ingredientes': ingredientes_list}, safe=False)

def ingredientes_extrusao(request):
    # Inicialmente, pegamos todos os objetos
    queryset = IngredienteOrdemServico.objects.all()

    # Obtemos os parâmetros de filtro da URL
    ordem_servico_id = request.GET.get('ordem_servico_id')
    produto_id = request.GET.get('produto_id')

    # Aplicamos os filtros conforme os parâmetros
    if ordem_servico_id:
        queryset = queryset.filter(ordemservico__id=ordem_servico_id)

    if produto_id:
        queryset = queryset.filter(produto__id=produto_id)

    # Preparamos o contexto para o template
    context = {
        'ingredientes': queryset
    }

    # Renderizamos o template com o contexto
    return render(request, 'add/ingredientes_extrusao.html', context)

def get_ingredientes(request):
    produto_id = request.GET.get('produto')
    ingredientes = IngredienteOrdemServico.objects.filter(produto_id=produto_id).select_related('ingrediente')

    ingredientes_list = []
    for ingrediente in ingredientes:
        ingredientes_list.append({
            'ingrediente': str(ingrediente.ingrediente),  # Assuming __str__ method is defined in Ingredientes model
            'qtde': ingrediente.qtde
        })

    return JsonResponse({'ingredientes': ingredientes_list})

def atualizar_extrusao(request, extrusao_id):
    extrusao = get_object_or_404(Extrusao, id=extrusao_id)

    if request.method == 'POST':
        form = ExtrusaoUpdateForm(request.POST, instance=extrusao)
        if form.is_valid():
            form.save()
            return redirect('lista_extrusao')
        else:
            print('form.invalid')
            print(form.errors)
    else:
        form = ExtrusaoUpdateForm(instance=extrusao)
        # Preencher automaticamente a data e hora de início se ainda não estiverem definidas
        if not extrusao.hora_inicio:
            extrusao.hora_inicio = timezone.localtime().time()
        if not extrusao.data_inicio:
            extrusao.data_inicio = timezone.localtime().date()
        extrusao.save()

    return render(request, 'add/atualizar_extrusao.html', {'form': form})
# -------------- Fim views de cadastro ------------------------


