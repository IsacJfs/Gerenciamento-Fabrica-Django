from typing import Any, Dict
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
from django import forms


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['codigo','cnpj_cpf', 'razao_social', 'nome_fantasia', 'celular', 'telefone', 'email', 'atividade_economica_profissao']
        widgets = {
            'cnpj_cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'razao_social': forms.TextInput(attrs={'class': 'form-control'}),
            'nome_fantasia': forms.TextInput(attrs={'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'atividade_economica_profissao': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean(self) -> Dict[str, Any]:
        return super().clean()

class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['rua', 'numero', 'complemento', 'cidade', 'estado', 'cep']
        widgets = {
            'rua': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'complemento': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
            'cep': forms.TextInput(attrs={'class': 'form-control'}),
        }

class OperadorForm(forms.ModelForm):
    class Meta:
        model = Operador
        fields = ['id', 'nome', 'cargo']
        widgets = {
            'id': forms.TextInput(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cargo': forms.TextInput(attrs={'class': 'form-control'}),
        }

class MaquinaExtrusaoForm(forms.ModelForm):
    class Meta:
        model = MaquinaExtrusao
        fields = ['id', 'marca', 'modelo']
        widgets = {
            'id': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'})
        }

class MaquinaImpressaoForm(forms.ModelForm):
    class Meta:
        model = MaquinaImpressao
        fields = ['id', 'marca', 'modelo']
        widgets = {
            'id': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'})
        }

class MaquinaCorteForm(forms.ModelForm):
    class Meta:
        model = MaquinaCorte
        fields = ['id', 'marca', 'modelo']
        widgets = {
            'id': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'})
        }

class ProdutoForm(forms.ModelForm):
    tipo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    cor_produto = forms.ModelChoiceField(queryset=CorProduto.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    acabamento_produto = forms.ModelChoiceField(queryset=Acabamento.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    tratamento_produto = forms.ModelChoiceField(queryset=Tratamento.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    material_produto = forms.ModelChoiceField(queryset=Material.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Produto
        fields = ['ordem_servico', 'tipo', 'cor_produto', 'acabamento_produto', 'tratamento_produto', 'material_produto']

class OrdemServicoForm(forms.ModelForm):
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    observacao = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = OrdemServico
        fields = ['cliente', 'observacao']

class TintaForm(forms.ModelForm):
    class Meta:
        model = Tinta
        fields = ['id', 'cor']
        widgets = {
            'id': forms.TextInput(attrs={'class': 'form-control'}),
            'cor': forms.TextInput(attrs={'class': 'form-control'})
        }

class TintaOrdemServicoForm(forms.ModelForm):
    class Meta:
        model = TintaOrdemServico
        fields = ['id', 'ordemservico', 'tinta']
        widgets = {
            'id': forms.TextInput(attrs={'class': 'form-control'}),
            'ordemservico': forms.Select(attrs={'class': 'form-control'}),
            'tinta': forms.Select(attrs={'class': 'form-control'})
        }

class IngredientesForm(forms.ModelForm):
    class Meta:
        model = Ingredientes
        fields = ['id', 'ingrediente']
        widgets = {
            'id': forms.TextInput(attrs={'class': 'form-control'}),
            'ingrediente': forms.TextInput(attrs={'class': 'form-control'})
        }

class IngredienteOrdemServicoForm(forms.ModelForm):
    ingrediente = forms.ModelChoiceField(queryset=Ingredientes.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    qtde = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = IngredienteOrdemServico  # Adicione esta linha para especificar o modelo
        fields = ['ingrediente', 'qtde']

class ExtrusaoForm(forms.ModelForm):
    operador = forms.ModelChoiceField(queryset=Operador.objects.all().distinct(), widget=forms.Select(attrs={'class': 'form-select'}))
    maquina_extrusao = forms.ModelChoiceField(queryset=MaquinaExtrusao.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
    hora_fim = forms.TimeField(input_formats=['%H:%M'], widget=forms.TimeInput(format='%H:%M', attrs={'class': 'form-control'}), required=False)
    data_fim = forms.DateField(input_formats=['%d/%m/%Y'],widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'form-control'}), required=False)
    produto_ingrediente = forms.ModelChoiceField(queryset=IngredienteOrdemServico.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
    status = forms.ChoiceField(choices=Extrusao.STATUS_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    tipo_produto = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    quantidade = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=False)
    desperdicio = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=False)

    class Meta:
        model = Extrusao
        fields = ['operador', 'maquina_extrusao', 'hora_fim', 'data_fim', 'produto_ingrediente', 'status', 'tipo_produto', 'quantidade', 'desperdicio']

class ImpressaoForm(forms.ModelForm):
    class Meta:
        model = Impressao
        fields = ['ordem_servico', 'operador', 'maquina_impressao', 'hora_inicio', 'hora_fim', 'data']
        widgets = {
            'ordem_servico': forms.Select(attrs={'class': 'form-control'}),
            'operador': forms.Select(attrs={'class': 'form-control'}),
            'maquina_impressao': forms.Select(attrs={'class': 'form-control'}),
            'hora_inicio': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'hora_fim': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'data': forms.DateInput(attrs={'class': 'form-control'})
        }

class CorteForm(forms.ModelForm):
    class Meta:
        model = Corte
        fields = ['ordem_servico', 'operador', 'maquina_corte', 'hora_inicio', 'hora_fim', 'data']
        widgets = {
            'ordem_servico': forms.Select(attrs={'class': 'form-control'}),
            'operador': forms.Select(attrs={'class': 'form-control'}),
            'maquina_corte': forms.Select(attrs={'class': 'form-control'}),
            'hora_inicio': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'hora_fim': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'data': forms.DateInput(attrs={'class': 'form-control'})
        }

class AcabamentoForm(forms.ModelForm):
    class Meta:
        model = Acabamento
        fields = ['acabamento_produto']
        widgets = {
            'acabamento_produto': forms.Select(attrs={'class': 'form-control'}),
        }

class TratamentoForm(forms.ModelForm):
    class Meta:
        model = Tratamento
        fields = ['tratamento_produto']
        widgets = {
            'tratamento_produto': forms.Select(attrs={'class': 'form-control'}),
        }

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['material_produto']
        widgets = {
            'material_produto': forms.Select(attrs={'class': 'form-control'}),
        }

class CorForm(forms.ModelForm):
    class Meta:
        model = CorProduto
        fields = ['cor_produto']
        widgets = {
            'cor_produto': forms.Select(attrs={'class': 'form-control'}),
        }

class ExtrusaoUpdateForm(ExtrusaoForm):
    operador = forms.ModelChoiceField(queryset=Operador.objects.all().distinct(), widget=forms.Select(attrs={'class': 'form-select'}), required=False)
    maquina_extrusao = forms.ModelChoiceField(queryset=MaquinaExtrusao.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}), required=False)
    produto_ingrediente = forms.ModelChoiceField(queryset=IngredienteOrdemServico.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}), required=False)
    class Meta(ExtrusaoForm.Meta):
        fields = ['hora_fim', 'data_fim', 'tipo_produto', 'quantidade', 'desperdicio', 'status']