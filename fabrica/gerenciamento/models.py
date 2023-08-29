from django.db import models
from django.utils import timezone

class Cliente(models.Model):
    codigo = models.AutoField(primary_key=True)
    cnpj_cpf = models.CharField(max_length=18, unique=True)
    razao_social = models.CharField(max_length=255)
    nome_fantasia = models.CharField(max_length=255, blank=True, null=True)
    telefone = models.CharField(max_length=15)
    celular = models.CharField(max_length=15)
    email = models.EmailField()
    atividade_economica_profissao = models.CharField(max_length=255)

    def __str__(self):
        nome = self.razao_social
        return nome

class Endereco(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    rua = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=50, blank=True, null=True)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    cep = models.CharField(max_length=10)

class Operador(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class MaquinaExtrusao(models.Model):
    id = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)

    def __str__(self):
        nome = self.marca
        return nome

class MaquinaImpressao(models.Model):
    id = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)

class MaquinaCorte(models.Model):
    id = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)

class Tratamento(models.Model):
    id = models.AutoField(primary_key=True)
    tratamento_produto = models.CharField(max_length=100)

    def __str__(self):
        return self.tratamento_produto

class Material(models.Model):
    id = models.AutoField(primary_key=True)
    material_produto = models.CharField(max_length=100)

    def __str__(self):
        return self.material_produto

class Acabamento(models.Model):
    id = models.AutoField(primary_key=True)
    acabamento_produto = models.CharField(max_length=100)

    def __str__(self):
        return self.acabamento_produto

class CorProduto(models.Model):
    id = models.AutoField(primary_key=True)
    cor_produto = models.CharField(max_length=100)

    def __str__(self):
        return self.cor_produto

class OrdemServico(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    observacao = models.CharField(max_length=100)
    data_inicio = models.DateField(auto_now_add=True)

    def __str__(self):
        valor = self.id
        nome = f'Orden nº({valor})'
        return nome

class Produto(models.Model):
    ordem_servico = models.ForeignKey(OrdemServico, related_name='produtos', on_delete=models.CASCADE)
    tipo = models.CharField(max_length=100)
    cor_produto = models.ForeignKey(CorProduto, on_delete=models.CASCADE)
    acabamento_produto = models.ForeignKey(Acabamento, on_delete=models.CASCADE)
    tratamento_produto = models.ForeignKey(Tratamento, on_delete=models.CASCADE)
    material_produto = models.ForeignKey(Material, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.tipo
    
class StatusServico(models.Model):
    ordem_servico = models.ForeignKey(OrdemServico, on_delete=models.CASCADE)
    operador = models.ForeignKey(Operador, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    hora_alteracao = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateField(auto_now_add=True)

class Tinta(models.Model):
    id = models.AutoField(primary_key=True)
    cor = models.CharField(max_length=50)

class TintaOrdemServico(models.Model):
    id = models.AutoField(primary_key=True)
    ordemservico = models.ForeignKey(OrdemServico, on_delete=models.CASCADE)
    tinta = models.ForeignKey(Tinta, on_delete=models.CASCADE)
    qtde = models.CharField(max_length=10)

class Ingredientes(models.Model):
    id = models.AutoField(primary_key=True)
    ingrediente = models.CharField(max_length=100)

    def __str__(self):
        return self.ingrediente

class IngredienteOrdemServico(models.Model):
    id = models.AutoField(primary_key=True)
    ordemservico = models.ForeignKey(OrdemServico, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, related_name='ingredientes_ordem_servico', on_delete=models.CASCADE)
    ingrediente = models.ForeignKey(Ingredientes, on_delete=models.CASCADE)
    qtde = models.FloatField()

    def __str__(self):
        ordem = self.ordemservico
        produto_ordem = self.produto
        nome = f'{ordem} - Produto: {produto_ordem}'
        return nome

class Extrusao(models.Model):
    STATUS_CHOICES = [
        ('iniciado', 'Iniciado'),
        ('finalizado', 'Finalizado'),
    ]

    operador = models.ForeignKey(Operador, on_delete=models.CASCADE)
    maquina_extrusao = models.ForeignKey(MaquinaExtrusao, on_delete=models.CASCADE)
    hora_inicio = models.TimeField(null=True, blank=True)
    data_inicio = models.DateField(null=True, blank=True)
    hora_fim = models.TimeField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)
    produto_ingrediente = models.ForeignKey(IngredienteOrdemServico, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='iniciado')
    tipo_produto = models.CharField(max_length=100, null=True, blank=True)
    quantidade = models.FloatField(null=True, blank=True)
    desperdicio = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.operador} - {self.maquina_extrusao} - {self.produto_ingrediente} - {self.status}"
    
    def save(self, *args, **kwargs):
        # Preenchimento automático de data_inicio e hora_inicio se eles não estiverem definidos
        if self.data_inicio is None:
            self.data_inicio = timezone.localtime().date()
        if self.hora_inicio is None:
            self.hora_inicio = timezone.localtime().time()
        super(Extrusao, self).save(*args, **kwargs)

class Impressao(models.Model):
    ordem_servico = models.ForeignKey(OrdemServico, on_delete=models.CASCADE)
    operador = models.ForeignKey(Operador, on_delete=models.CASCADE)
    maquina_impressao = models.ForeignKey(MaquinaImpressao, on_delete=models.CASCADE)
    hora_inicio = models.DateTimeField()
    hora_fim = models.DateTimeField()
    data = models.DateField()

class Corte(models.Model):
    ordem_servico = models.ForeignKey(OrdemServico, on_delete=models.CASCADE)
    operador = models.ForeignKey(Operador, on_delete=models.CASCADE)
    maquina_corte = models.ForeignKey(MaquinaCorte, on_delete=models.CASCADE)
    hora_inicio = models.DateTimeField()
    hora_fim = models.DateTimeField()
    data = models.DateField()

class ProdutoImpressao(models.Model):
    id = models.AutoField(primary_key=True)
    ordemservico = models.ForeignKey(OrdemServico, on_delete=models.CASCADE)
    item_produzido = models.ForeignKey(Impressao, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=10)
    qtde = models.CharField(max_length=10)
    peso = models.CharField(max_length=10)

class ProdutoCorte(models.Model):
    id = models.AutoField(primary_key=True)
    ordemservico = models.ForeignKey(OrdemServico, on_delete=models.CASCADE)
    item_produzido = models.ForeignKey(Corte, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=10)
    qtde = models.CharField(max_length=10)
    peso = models.CharField(max_length=10)